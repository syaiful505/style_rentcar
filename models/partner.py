from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Partner(models.Model):
    _inherit = 'res.partner'

    is_pegawainya = fields.Boolean(
        string='Pegawai', 
        default=False
    )
    is_customernya = fields.Boolean(
        string='Customer', 
        default=False
    )
    is_menikah = fields.Boolean(
        string='Sudah menikah',
        default=False
    )
    @api.constrains('name')
    def _check_name(self):
        for record in self :
            same = self.env['res.partner'].search([('name', '=',record.name), ('id', '!=',record.id)])
            if same:
                raise ValidationError("Nama %s sudah ada" % record.name)    