#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class matpel(models.Model):

    _name = "skripsi.matpel"
    _description = "skripsi.matpel"
    name = fields.Char( required=True, string="Nama Mata Pelajaran",  help="")
    kode = fields.Char( string="Kode Mata Pelajaran",  help="")

    matpel_ids = fields.One2many(comodel_name="skripsi.absen_madin", inverse_name="matpel_id", string="Absen")
    detile_jadwal_madin_ids = fields.One2many(comodel_name="skripsi.detile_jadwal_madin",  inverse_name="matpel_id",  string="Detile Jadwal Madin",  help="")
    detile_jadwal_madrasah_ids = fields.One2many(comodel_name="skripsi.detile_jadwal_madrasah",  inverse_name="matpel_id",  string="Detile Jadwal Madrasah",  help="")
    materi_madrasah_ids = fields.One2many(comodel_name="skripsi.materi_madrasah",  inverse_name="matpel_id",  string="Materi Madrasah",  help="")