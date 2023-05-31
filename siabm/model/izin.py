#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class izin(models.Model):

    _name = "skripsi.izin"
    _description = "skripsi.izin"
    name = fields.Date( required=True, string="Tanggal",  help="")
    lama = fields.Char( string="Lama Izin",  help="")
    keperluan = fields.Char( string="Keperluan Izin",  help="")
    catatan = fields.Char( string="Catatan",  help="")


    siswa_id = fields.Many2one(comodel_name="skripsi.siswa",  string="Nama Siswa",  help="")
