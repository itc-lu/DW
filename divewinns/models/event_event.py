from odoo import api, models, fields

class EventEvent(models.Model):
    _name = "event.event"
    _inherit = "event.event"

    training_dates_ids = fields.One2many(comodel_name="divewinns.training.date", inverse_name="event_id", string="Dates of Training")
    instructor_id = fields.Many2one(comodel_name="hr.employee")
    