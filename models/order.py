from odoo import api, fields, models

class OrderMobil(models.Model):
    _name = 'stylerent.ordermobil'
    _description = 'New Description'

    pemesan_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Nama Pemesan',
        domain=[('is_customernya','=','True')]
    )
    tanggal_pesan = fields.Datetime(
        string='Tanggal pesanan',
        default=fields.Datetime.now
    )
    #membuat viewnya detail field order
    detailjenis_ids = fields.One2many(
        comodel_name='stylerent.detailorder', 
        inverse_name='order_id', 
        string='Detail Pesanan'
    )

class DetailOrder(models.Model):
    _name = 'stylerent.detailorder'
    _description = 'Detail Orderan Customer'

    name = fields.Char(
        string='Kode Order'
    )
    order_id = fields.Many2one(
        comodel_name='stylerent.ordermobil',
        string='Order Mobil'
    )
    jenissewa_id = fields.Many2one(
        comodel_name='stylerent.jenismobil', 
        string='Jenis Sewa Mobil'
    )
    lamasewa = fields.Integer(
        string='Lama sewa'
    )
    harga = fields.Integer(
        compute='_compute_harga', 
        string='Harga Sewa'
    )
    
    @api.depends('jenissewa_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.jenissewa_id.harga
    
    jumlahnya = fields.Integer(compute='_compute_jumlahnya', string='Total harga sewa')
    
    @api.depends('lamasewa')
    def _compute_jumlahnya(self):
        for record in self:
            record.jumlahnya = record.harga * record.lamasewa