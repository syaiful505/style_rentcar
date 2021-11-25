from odoo import api, fields, models

class Suplier(models.Model):
    _name = 'stylerent.suplier'
    _description = 'Data Suplier'

    name = fields.Char(string='Nama Suplier')
    cp = fields.Char(string='Contact Person')
    alamat = fields.Char(string='Alamat Suplier')
    telp = fields.Char(string='No telefon')

    maintenance = fields.One2many(comodel_name='stylerent.maintenance', inverse_name='suplier', string='Alat Bahan Maintenance')