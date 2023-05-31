#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class detile_kelas_madin(models.Model):

    _name = "skripsi.detile_kelas_madin"
    _description = "skripsi.detile_kelas_madin"
    name = fields.Char( required=True, string="Nama Kelas",  help="")
    tahun_ajaran = fields.Selection(selection=[('01','2021'),('02','2022'),('03','2023')],  string="Tahun Ajaran",  help="")
    semester = fields.Selection(selection=[('01','Genap'),('02','Ganjil')],  string="Semester",  help="")
    grade = fields.Selection( selection=[('01','Basic'),('02','Middel'),('03','Expert')], string="Grade",  help="")

    absen_madin_ids = fields.One2many(comodel_name="skripsi.absen_madin",  inverse_name="detile_kelas_madin_id",  string="Absen Madin",  help="") 
    detile_jadwal_madin_ids = fields.One2many(comodel_name="skripsi.detile_jadwal_madin",  inverse_name="detile_kelas_madin_id",  string="Kelas Madin",  help="")
    materi_madin_ids = fields.One2many(comodel_name="skripsi.materi_madin",  inverse_name="detile_kelas_madin_id",  string="Materi",  help="")
    ustadz_id = fields.Many2one(comodel_name="skripsi.ustadz",  string="Ustadz",  help="")
    siswa_ids = fields.Many2many('skripsi.siswa','detail_kelas_madin_siswa_rel','detail_kelas_madin_id','siswa_id', string='Daftar Siswa')

