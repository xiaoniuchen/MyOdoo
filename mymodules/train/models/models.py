# -*- coding: utf-8 -*-

from odoo import models, fields, api

class train(models.Model):
    _name = 'train.train'
    _description = 'train.train'

    name = fields.Char(string=u'课程',required=True)
    teacher = fields.Many2one('res.users', string='培训教师')
    date_train = fields.Datetime(string=u'培训日期',default=fields.Datetime.now)
    num_student = fields.Integer(string='应出勤人数')
    train_line = fields.One2many('train.train_line','train_id')


class train_line(models.Model):
    _name = 'train.train_line'
    _description = 'train.train_line'

    train_id = fields.Many2one('train.train')
    student = fields.Many2one('res.users', string='培训学生')
    is_buy = fields.Boolean(string = '是否购买课程')
    wherefrom = fields.Selection([
        ('web', '网站'),
        ('QQ', 'QQ'),
        ('WeiXin', '微信')
    ],)





