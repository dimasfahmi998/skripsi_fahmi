#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class detile_jadwal_madrasah(models.Model):

    _name = "skripsi.detile_jadwal_madrasah"
    _description = "skripsi.detile_jadwal_madrasah"
    name = fields.Char( required=True, string="Hari",  help="")
    jamke = fields.Char( string="Jamke",  help="")


    matpel_id = fields.Many2one(comodel_name="skripsi.matpel",  string="Mata Pelajaran",  help="")
    guru_id = fields.Many2one(comodel_name="skripsi.guru",  string="Guru",  help="")
    detile_kelas_madrasah_id = fields.Many2one(comodel_name="skripsi.detile_kelas_madrasah",  string="Kelas",  help="")
