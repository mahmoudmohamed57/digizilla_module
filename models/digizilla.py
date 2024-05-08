from odoo import models, fields, api

class Tag(models.Model):
    _name = 'digizilla.tag'
    _inherit = 'mail.thread'
    _description = 'Digizilla Tag'

    name = fields.Char(string='Name', required=True)

class Digizilla(models.Model):
    _name = 'digizilla'
    _description = 'Digizilla Model'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    country = fields.Char(string='Country')
    joining_date = fields.Date(string='Joining Date')
    tags = fields.Many2many('digizilla.tag', string='Tags', widget='many2many_tags')
    customers = fields.Many2many('res.partner', string='Customers')
    company_id = fields.Many2one('res.company', string='Company', required=True)
    notes = fields.Text(string='Notes')
    comments = fields.Char(string='Comments')
    
    @api.model
    def default_get(self, fields):
        defaults = super(Digizilla, self).default_get(fields)
        defaults['company_id'] = self.env.company.id
        return defaults
    
    @api.model
    def create(self, vals):
        rec = super(Digizilla, self).create(vals)
        rec.message_post(body="New record created: %s" % rec.name)
        return rec

    def write(self, vals):
        old_values = {field: getattr(self, field) for field in vals.keys()}
        res = super(Digizilla, self).write(vals)
        for field, value in vals.items():
            if field != 'message_ids':
                if field in old_values:
                    self.message_post(body="Field %s changed from %s to %s" % (field, old_values[field], value))
                else:
                    self.message_post(body="Field %s set to %s" % (field, value))
        return res

    def generate_report(self):
        report_data = {'records': self}
        return self.env.ref('digizilla_module.digizilla_report_template').report_action(self, data=report_data)
    