from odoo import models, fields, api
    
#nama class dibiarin tidak masalah yg penting _name nya bedain
class stylerent(models.Model): 
    _name = "stylerent.service"
    _description = "Teknik Pemeliharaan mobil"

    name = fields.Selection(
        string='Jenis Service',
        selection=[('biasa', 'biasa'), ('istimewa', 'istimewa'), ('spesial', 'spesial'), ('super','super')]
    )
    teknik = fields.Selection(
        string='Teknik service',
        selection=[('Large', 'All'), ('Medium', 'Machine'), ('Small', 'Oil')]
    )
    hasil = fields.Selection(
        string='Hasil Service',
        selection=[('Ringan', 'Ringan'), ('Sedang', 'Sedang'), ('Berat', 'Berat')]
    )
    tersedia = fields.Boolean(
        string='tersedia',
        default=True
    )
    deskripsiservice = fields.Char(
        string='deskripsi',
        help='Isi dengan Service dari mobil'
    )
    models_id = fields.One2many(
        comodel_name='stylerent.jenismobil', 
        inverse_name='service_id',
        string='Deskripsi Mobil'
    )
    pegawainya_id = fields.Many2one(
        comodel_name='res.partner',
        string='Penanggung Jawab',
        domain=[('is_pegawainya','=','True')]
        
    )
    