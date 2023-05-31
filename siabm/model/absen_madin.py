#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class absen_madin(models.Model):

    _name = "skripsi.absen_madin"
    _description = "skripsi.absen_madin"
    name = fields.Date( required=True, string="Tanggal", default=fields.Date.context_today,  help="")
    detile_kelas_madin_id = fields.Many2one(comodel_name="skripsi.detile_kelas_madin",  string="Kelas Madin",  help="")
    absen_ids = fields.One2many(comodel_name="skripsi.absen",  inverse_name="absen_madin_id",  string="Absen",  help="")
    matpel_id = fields.Many2one('skripsi.matpel', 'Mata Pelajaran')
    semester = fields.Selection([('gasal', 'Semester Gasal'), ('genap', 'Semester Genap')], 'Semester')
    
class penilaian_line(models.Model):
    _name = 'penilaian.line'

    penilaian_id = fields.Many2one('skripsi.absen_madin', 'Penilaian Kehadiran', required=True, ondelete='cascade')

