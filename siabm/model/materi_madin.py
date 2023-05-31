from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class materi_madin(models.Model):

    _name = "skripsi.materi_madin"
    _description = "skripsi.materi_madin"
    name = fields.Char(string="Nama Materi",  help="")
    materi = fields.Binary(string="Materi",  help="")
    materi_name = fields.Char(string="Nama Materi",  help="")

    detile_kelas_madin_id = fields.Many2one(comodel_name="skripsi.detile_kelas_madin",  string="Detile Kelas Madin",  help="")

