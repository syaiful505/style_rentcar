from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ModelDasar(models.Model):
    _name = "stylerent.modeldasar"
    _description = "model dasar style rent car"
    
    kapasitas = fields.Char(
        string='kapasitas penumpang',
        Required=True,
    )
    tipe = fields.Selection(
        string='tipe/jenis mobil',
        selection=[('sedan', 'Sedan'), ('lcgc', 'LCGC'), ('mpv', 'MPV'), ('suv', 'SUV')]
    )
    
class stylerent(models.Model):
    _name = "stylerent.jenismobil"
    _description = "Daftar Jenis-jenis mobil"
    _inherit = 'stylerent.modeldasar' #memanggil model class yg atas inheriten delegation

    name = fields.Char(
        string='Jenis Sewa',
        Required=True
    )
    harga = fields.Integer(
        string='Harga sewa',
        Required=True
    )
    active = fields.Boolean(
        default=True
    )
    service_id = fields.Many2one(
        comodel_name='stylerent.service', 
        string='Pemeliharaan',
        Required=True, 
        delegate=True
    )
    
    @api.onchange('tipe')
    def _onchange_tipe(self):
        if self.tipe == 'mpv':
            return {
                'warning' : {
                    'title' : "Teknik Pemeliharaan",
                    'message' : "Rubah teknik pemeliharaan ke istimewa"
                },
            }
        elif self.tipe == 'suv':
            return {
                'warning' : {
                    'title' : "Teknik Pemeliharaan",
                    'message' : "Rubah teknik pemeliharaan ke super"
                }
            }