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

    jml_order = fields.Integer(compute='_compute_jml_order', string='Total Order')
    
    @api.depends('detailjenis_ids')
    def _compute_jml_order(self):
        for record in self:
            record.jml_order += len(record.detailjenis_ids)

    total_order = fields.Integer(compute='_compute_total_order', string='Total yang harus dibayar')
    
    @api.model
    def _compute_total_order(self):
        for record in self:
            total = sum(self.env['stylerent.detailorder'].search([]).mapped('jumlahnya'))
            record.total_order = total

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