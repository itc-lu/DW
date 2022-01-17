from odoo import api, models, fields


class TrainingDate(models.Model):
    _name = "divewinns.training.date"
    _description = "Date of training"

    name = fields.Char(string="Name", required=True,
                       default=lambda self: self.event_id.name)
    start = fields.Datetime(string="Start Date", required=True)
    end = fields.Datetime(string="End Date", required=True)
    description = fields.Text(string="Description", required=True)
    room = fields.Selection(string="Room", required=True, selection=[("training1", "Trainingsroom 1"), ("training2", "Trainingsroom 2"), ("community", "Community"), ("pool", "Pool"), ("bus", "Bus")])
    room_availability = fields.Selection(string="Availability", selection=[("0", 'Unavailable'), ('1', 'Available')], compute="_compute_room_availability")
    overlapping_count = fields.Integer(string="Number of overlaps", compute="_compute_room_availability")

    event_id = fields.Many2one(comodel_name="event.event", string="Event")
    calendar_event_id = fields.Many2one(comodel_name="calendar.event", string="Calendar event")

    organizer_id = fields.Many2one(comodel_name="res.users", string="Organizer",
                                   required=True, default=lambda self: self.event_id.instructor_id.user_id.id)
    #partner_ids = fields.Many2many(comodel_name="res.partner", string="Attendees")

    @api.model
    def create(self, vals):
        obj = super(TrainingDate, self).create(vals)
        alarm_id = self.env["calendar.alarm"].search(
            [('alarm_type', '=', 'email'), ('duration', '=', 1), ('interval', '=', 'days')])
        if not alarm_id:
            alarm_id = self.env["calendar.alarm"].create({
                'name': "E-mail 1 Day",
                'alarm_type': 'email',
                'duration': 1,
                'interval': 'days',
            })
        calendar_event = self.env["calendar.event"].create({
            "name": obj.name,
            "start": obj.start,
            "stop": obj.end,
            "user_id": obj.organizer_id.id,
            "event_id": obj.event_id.id,
            "partner_ids": obj.event_id.registration_ids.partner_id,
            "alarm_ids": [(4, alarm_id.id)],
            "room": obj.room,
        })
        calendar_event.partner_ids = [(4, obj.organizer_id.partner_id.id)]
        obj.calendar_event_id = calendar_event.id
        return obj

    @api.onchange("event_id")
    def _on_event_changed(self):
        for training_date in self:
            training_date.name = training_date.event_id.name
            training_date.organizer_id = training_date.event_id.instructor_id.user_id.id

    @api.onchange('start', 'end')
    def _on_date_changed(self):
        for training_date in self:
            training_date.calendar_event_id.start = training_date.start
            training_date.calendar_event_id.stop = training_date.end

    @api.depends('room', 'start', 'end')
    def _compute_room_availability(self):
        for training_date in self:
            if training_date.start and training_date.end and training_date.room:
                overlapping_training_dates = self.env["divewinns.training.date"].search([
                    ('room', '=', training_date.room),
                    ('id', '!=', training_date._origin.id),
                    '|', '|',
                    '&', ('start', '<=', training_date.start), ('end','>=', training_date.start),
                    '&', ('start', '<=', training_date.end), ('end','>=', training_date.end),
                    '&', ('start', '>=', training_date.start), ('start', '<=', training_date.end),
                ])
                training_date.room_availability = '1' if len(overlapping_training_dates) == 0 else '0'
                training_date.overlapping_count = len(overlapping_training_dates)
            else:
                training_date.room_availability = '1'
                training_date.overlapping_count = 0

    def action_get_overlapping(self):
        for training_date in self:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Training dates',
                'view_mode': 'calendar',
                'res_model': 'divewinns.training.date',
                'domain': [
                    ('room', '=', training_date.room),
                ],
            }
