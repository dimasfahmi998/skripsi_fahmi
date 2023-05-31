#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning


class siswa(models.Model):

    
    _name = "skripsi.siswa"
    _description = "skripsi.siswa"
    name = fields.Char(required=True, string="Nama Siswa",  help="") 
    
    nis = fields.Char( string="NIS",  help="")
    nisn = fields.Char( string="NISN",  help="")
    email = fields.Char(string="Email",  help="")
    alamat = fields.Char( string="Alamat",  help="")
    no_telfon = fields.Char( string="No telfon",  help="")
    agama = fields.Selection(selection=[('01','Islam'),('02','Protestan'),('03','Katolik'),('04','Hindu'),('05','Buddha'),('06','Khonghucu')],  string="Agama",  help="")
    gender = fields.Selection(selection=[('01','Laki-Laki'),('02','Perempuan')],  string="Jenis Kelamin",  help="")
    tanggal_lahir = fields.Date( string="Tanggal Lahir",  help="")
    tempat_lahir = fields.Char( string="Tempat Lahir",  help="")
    nama_ayah = fields.Char( string="Nama Ayah",  help="")
    nama_ibu = fields.Char( string="Nama Ibu",  help="")

    izin_ids = fields.One2many(comodel_name="skripsi.izin",  inverse_name="siswa_id",  string="Perizinan Siswa",  help="")
    pelanggaran_madin_ids = fields.One2many(comodel_name="skripsi.pelanggaran_madin",  inverse_name="siswa_id",  string="Pelanggaran Madin",  help="")
    pelanggaran_madrasah_ids = fields.One2many(comodel_name="skripsi.pelanggaran_madrasah",  inverse_name="siswa_id",  string="Penlanggaran Madrasah",  help="")
    pelanggaran_pesantren_ids = fields.One2many(comodel_name="skripsi.pelanggaran_pesantren",  inverse_name="siswa_id",  string="Penlanggaran Pesantren",  help="")
    absen_ids = fields.One2many(comodel_name="skripsi.absen",  inverse_name="siswa_id",  string="Absen",  help="")
