#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class absen_madrasah(models.Model):

    _name = "skripsi.absen_madrasah"
    _description = "skripsi.absen_madrasah"
    name = fields.Date( required=True, string="Tanggal",  help="")


    absen_ids = fields.One2many(comodel_name="skripsi.absen",  inverse_name="absen_madrasah_id",  string="Absen",  help="")
    detile_kelas_madrasah_id = fields.Many2one(comodel_name="skripsi.detile_kelas_madrasah",  inverse_name="absen_madrasah_ids",  string="Kelas",  help="")
    # detile_kelas_madrasah_id = fields.Many2one(comodel_name="skripsi.detile_kelas_madrasah",  string="Detile kelas madrasah",  help="")
