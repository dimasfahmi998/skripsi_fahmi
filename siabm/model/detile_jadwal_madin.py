#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class detile_jadwal_madin(models.Model):

    _name = "skripsi.detile_jadwal_madin"
    _description = "skripsi.detile_jadwal_madin"
    name = fields.Char( required=True, string="Hari",  help="")
    jamke = fields.Char( string="Jamke",  help="")


    matpel_id = fields.Many2one(comodel_name="skripsi.matpel",  string="Mata Pelajaran",  help="")
    ustadz_id = fields.Many2one(comodel_name="skripsi.ustadz",  string="Ustadz",  help="")
    detile_kelas_madin_id = fields.Many2one(comodel_name="skripsi.detile_kelas_madin",  string="Kelas",  help="")
