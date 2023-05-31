from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class detile_materi_madrasah(models.Model):

    _name = "skripsi.detile_materi_madrasah"
    _description = "skripsi.detile_materi_madrasah"
    name = fields.Char(string="Nama Materi",  help="")
    materi = fields.Binary(string="Materi",  help="")
    materi_name = fields.Char(string="Nama Materi",  help="")

    materi_madrasah_id = fields.Many2one(comodel_name="skripsi.materi_madrasah",  string="Materi",  help="")

    