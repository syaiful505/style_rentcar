from odoo import api, fields, models


class stokmaintenance(models.Model):
    _name = 'stylerent.maintenance'
    _description = 'New Description'

    name = fields.Char(string='Name')
