# -*- coding: utf-8 -*-

from odoo import models, fields, api

class teacher(models.Model):
     _name = 'xksystem.teacher'
     _description = 'xksystem.teacher'

     name = fields.Char(string='教师姓名')
     code = fields.Char(string='教师编号')