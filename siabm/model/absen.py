#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class absen(models.Model):

    _name = "skripsi.absen"
    _description = "skripsi.absen"
    name = fields.Selection(selection=[('01','Hadir'),('02','Izin'),('03','Sakit'),('04','Alfa')],  required=True, string="Status Kehadiran",  help="")

    siswa_id = fields.Many2one(comodel_name="skripsi.siswa",  string="Siswa",  help="")
    absen_madin_id = fields.Many2one(comodel_name="skripsi.absen_madin",  string="Absen Mdin",  help="")
    absen_madrasah_id = fields.Many2one(comodel_name="skripsi.absen_madrasah",  string="Absen Madrasah",  help="")

    siswa_id_nis = fields.Char(related='siswa_id.nis', string='NIS')
