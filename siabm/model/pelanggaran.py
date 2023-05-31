from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class pelanggaran(models.Model):

    _name = "skripsi.pelanggaran"
    _description = "skripsi.pelanggaran"
    name = fields.Char( required=True, string="Nama Pelanggaran",  help="")
    tingkat_pelanggaran = fields.Selection(selection=[('01','Ringan'),('02','Sedang'),('03','Berat')],  string="Tingkat Pelanggaran",  help="")
    poin = fields.Selection(selection=[('01','5'),('02','15'),('03','20')],  string="Poin Pelanggaran",  help="")

    pelanggaran_pesantren_ids = fields.One2many(comodel_name="skripsi.pelanggaran_pesantren",  inverse_name="pelanggaran_id",  string="Pelanggaran Pesantren",  help="")
    pelanggaran_madin_ids = fields.One2many(comodel_name="skripsi.pelanggaran_madin",  inverse_name="pelanggaran_id",  string="Pelanggaran Madin",  help="")
    pelanggaran_madrasah_ids = fields.One2many(comodel_name="skripsi.pelanggaran_madrasah",  inverse_name="pelanggaran_id",  string="Pelanggaran Madrasah",  help="")