#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class pengasuh(models.Model):

    _name = "skripsi.pengasuh"
    _description = "skripsi.pengasuh"
    name = fields.Char( required=True, string="Name",  help="")
    alamat = fields.Char( string="Alamat",  help="")
    agama = fields.Selection(selection=[('01','Islam'),('02','Protestan'),('03','Katolik'),('04','Hindu'),('05','Buddha'),('06','Khonghucu')],  string="Agama",  help="")
    email = fields.Char( string="Email",  help="")
    no_telfon = fields.Char( string="No telfon",  help="")
    gender = fields.Selection(selection=[('01','Laki-Laki'),('02','Perempuan')],  string="Gender",  help="")
    pendidikan_terakhir = fields.Selection(selection=[('01','SD'),('02','SMP'),('03','SMA'),('04','S1'),('05','S2'),('06','S3')],  string="Pendidikan terakhir",  help="")
    tempat_lahir = fields.Char( string="Tempat lahir",  help="")
    tanggal_lahir = fields.Date( string="Tanggal lahir",  help="")


    kamar_ids = fields.One2many(comodel_name="skripsi.kamar",  inverse_name="pengasuh_id",  string="Kamar",  help="")
