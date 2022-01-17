from odoo import api, models, fields

class CalendarEvent(models.Model):
    _name = "calendar.event"
    _inherit = "calendar.event"

    event_id = fields.Many2one(comodel_name="event.event", string="Related event")
    room = fields.Char(string="Room")

    