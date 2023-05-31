#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class ustadz(models.Model):

    _name = "skripsi.ustadz"
    _description = "skripsi.ustadz"
    name = fields.Char( required=True, string="Nama",  help="")
    alamat = fields.Char( string="Alamat",  help="")
    no_telfon = fields.Char( string="No Telfon",  help="")
    email = fields.Char( string="Email",  help="")
    agama = fields.Selection(selection=[('01','Islam'),('02','Protestan'),('03','Katolik'),('04','Hindu'),('05','Buddha'),('06','Khonghucu')],  string="Agama",  help="")
    gender = fields.Selection(selection=[('01','Laki-Laki'),('02','Perempuan')],  string="Jenis Kelamin",  help="")
    keahlian = fields.Char( string="Keahlian",  help="")
    pendidikan_terakhir = fields.Selection(selection=[('01','SD'),('02','SMP'),('03','SMA'),('04','S1'),('05','S2'),('06','S3')],  string="Pendidikan Terakhir",  help="")
    tanggal_lahir = fields.Date( string="Tanggal Lahir",  help="")
    tempat_lahir = fields.Char( string="Tempat Lahir",  help="")


    detile_jadwal_madin_ids = fields.One2many(comodel_name="skripsi.detile_jadwal_madin",  inverse_name="ustadz_id",  string="Detile Jadwal Madin",  help="")
    detile_kelas_madin_ids = fields.One2many(comodel_name="skripsi.detile_kelas_madin",  inverse_name="ustadz_id",  string="Detile Kelas Madin",  help="")
