from odoo import api, fields, models


class maintenance(models.Model):
    _name = 'stylerent.maintenance'
    _description = 'Alat Bahan Maintenance'

    name = fields.Char(string='Nama')
    jenis = fields.Selection(string='Jenis', selection=[('bahan', 'Bahan'), ('alat', 'Alat')])
    harga = fields.Integer(string='Harga')
    stok = fields.Integer(string='Stok')
    
    suplier = fields.Many2one(comodel_name='stylerent.suplier', string='Supliernya')

    telp = fields.Char(compute='_compute_telp', string='No.Telepon')
    
    @api.depends('suplier')
    def _compute_telp(self):
        for record in self:
            record.telp = record.suplier.telp