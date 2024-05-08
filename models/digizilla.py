from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class Digizilla(models.Model):
    _name = 'digizilla'
    _description = 'Digizilla Model'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    country = fields.Char(string='Country')
    joining_date = fields.Date(string='Joining Date')
    tags = fields.Char(string='Tags')
    customers = fields.Many2many('res.partner', string='Customers')
    company_id = fields.Many2one('res.company', string='Company', required=True)
    notes = fields.Text(string='Notes')
    comments = fields.Char(string='Comments')

    @api.model
    def create(self, vals):
        rec = super(Digizilla, self).create(vals)
        _logger.info('New record created: %s', rec)
        return rec

    def write(self, vals):
        old_values = {field: getattr(self, field) for field in vals.keys()}
        res = super(Digizilla, self).write(vals)
        for field, value in vals.items():
            _logger.info('Field %s changed from %s to %s', field, old_values[field], value)
        return res
    
    def generate_report(self):
        data = {'docs': self}
        return self.env.ref('digizilla_module.report_digizilla').report_action(self, data=data)
