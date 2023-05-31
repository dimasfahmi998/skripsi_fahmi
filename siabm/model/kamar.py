#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class kamar(models.Model):

    _name = "skripsi.kamar"
    _description = "skripsi.kamar"
    name = fields.Char( required=True, string="Nama Kamar",  help="")


    pengasuh_id = fields.Many2one(comodel_name="skripsi.pengasuh",  string="Pengasuh",  help="")
    list_siswa_ids = fields.One2many(comodel_name="skripsi.list_siswa",  inverse_name="kamar_id",  string="List Siswa",  help="")
    siswa_ids = fields.Many2many('skripsi.siswa','kamar_siswa_rel','kamar_id','siswa_id', string='Daftar Siswa')
