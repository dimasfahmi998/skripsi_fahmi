#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class detile_kelas_madrasah(models.Model):

    _name = "skripsi.detile_kelas_madrasah"
    _description = "skripsi.detile_kelas_madrasah"
    name = fields.Char( required=True, string="Nama Kelas",  help="")
    tahun_ajaran = fields.Selection(selection=[('01','2021'),('02','2022'),('03','2023')],  string="Tahun ajaran",  help="")
    semester = fields.Selection(selection=[('01','Genap'),('02','Ganjil')],  string="Semester",  help="")


    guru_id = fields.Many2one(comodel_name="skripsi.guru",  string="Guru",  help="")
    absen_madrasah_ids = fields.One2many(comodel_name="skripsi.absen_madrasah",  inverse_name="detile_kelas_madrasah_id",  string="Absen Madrasah",  help="")
    detile_jadwal_madrasah_ids = fields.One2many(comodel_name="skripsi.detile_jadwal_madrasah",  inverse_name="detile_kelas_madrasah_id",  string="Kelas Madrasah",  help="")
    materi_madrasah_ids = fields.One2many(comodel_name="skripsi.materi_madrasah",  inverse_name="detile_kelas_madrasah_id",  string="Materi",  help="")
    siswa_ids = fields.Many2many('skripsi.siswa','detail_kelas_madrasah_siswa_rel','detail_kelas_madrasah_id','siswa_id', string='Daftar Siswa')
