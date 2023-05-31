#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class pelanggaran_madrasah(models.Model):

    _name = "skripsi.pelanggaran_madrasah"
    _description = "skripsi.pelanggaran_madrasah"
    name = fields.Char( string="Keterangan",  help="")
    tanggal = fields.Date( string="Tanngal Pelanggaran",  help="")

    pelanggaran_id = fields.Many2one(comodel_name="skripsi.pelanggaran",  string="Pelanggaran",  help="")
    pelanggaran_id_tingkat_pelanggaran = fields.Selection(related='pelanggaran_id.tingkat_pelanggaran', string='Tingkat Pelanggaran')
    pelanggaran_id_poin = fields.Selection(related='pelanggaran_id.poin', string='Poin')

    siswa_id = fields.Many2one(comodel_name="skripsi.siswa",  string="Siswa",  help="")
    siswa_id_nis = fields.Char(related='siswa_id.nis', string='NIS')

