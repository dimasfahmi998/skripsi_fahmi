#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class list_siswa(models.Model):

    _name = "skripsi.list_siswa"
    _description = "skripsi.list_siswa"
    name = fields.Char(string="Nama",  help="")


    siswa_id = fields.Many2one(comodel_name="skripsi.siswa",  string="Siswa",  help="")
    # absen_ids = fields.One2many(comodel_name="skripsi.absen",  inverse_name="list_siswa_id",  string="Absen",  help="")
    
    kamar_id = fields.Many2one(comodel_name="skripsi.kamar",  string="Kamar",  help="")
    # detile_kelas_madin_id = fields.Many2one(comodel_name="skripsi.detile_kelas_madin",  string="Detile Kelas Madin",  help="")
    # detile_kelas_madrasah_id = fields.Many2one(comodel_name="skripsi.detile_kelas_madrasah",  string="Detile Kelas Madrasah",  help="")
