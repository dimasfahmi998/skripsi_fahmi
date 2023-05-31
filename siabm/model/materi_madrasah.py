from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class materi_madrasah(models.Model):

    _name = "skripsi.materi_madrasah"
    _description = "skripsi.materi_madrasah"
    name = fields.Char(string="Nama Materi",  help="")
    
    
    detile_kelas_madrasah_id = fields.Many2one(comodel_name="skripsi.detile_kelas_madrasah",  string="Kelas",  help="")
    matpel_id = fields.Many2one(comodel_name="skripsi.matpel",  string="Mata Pelajaran",  help="")
    detile_materi_madrasah_ids = fields.One2many(comodel_name="skripsi.detile_materi_madrasah",  inverse_name="materi_madrasah_id",  string="Materi",  help="")