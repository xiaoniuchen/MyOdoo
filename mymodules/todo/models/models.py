# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.modules.module import get_module_resource
from odoo import tools, _


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = '待办事项'

    name = fields.Char('描述', required=True)
    is_done = fields.Boolean('已完成?', default=False)
    deadline = fields.Datetime(u'截止时间')
    category_id = fields.Many2one('todo.category', string=u'分类')
    priority = fields.Selection([
        ('todo', '待办'),
        ('normal', '普通'),
        ('urgency', '紧急')
    ], default='todo', string='紧急程度')
    state = fields.Selection([
        ('0', '未审核'),
        ('1', '审核')
    ], default='0', string='单据状态', readonly=1)
    is_expired = fields.Boolean(u'已过期', compute='_compute_is_expired')

    @api.depends('deadline')
    @api.multi
    def _compute_is_expired(self):
        for record in self:
            if record.deadline:
                record.is_expired = record.deadline < fields.Datetime.now()
            else:
                record.is_expired = False

    @api.multi
    def active_btn(self):
        return self.write({'state': '1'})

    @api.multi
    def draft_btn(self):
        return self.write({'state': '0'})

    @api.multi
    def write(self, vals):
        #uid = self.env.uid
        #print(uid)
        print("测试点击按钮！")
        todotask = self.env['todo.task'].search([('name', '=', 'User_todotask')])
        print(self)
        print(self.name)
        print(self.write_date)
        print(self.write_uid)
        print(self.is_done)
        print("--------------")
        print(todotask)
        print(todotask.name)
        print(todotask.write_date)
        print(todotask.write_uid)
        print(todotask.is_done)
        if (self.write_date != todotask.write_date) or (self.write_uid != todotask.write_uid):
            raise UserError(('单据已被他人修改,请知晓！'))
        if self.state=='1' and 'state' not in vals:
            raise UserError(('单据已审核,不能修改！'))
        return super(TodoTask, self).write(vals)

class TodoCategory(models.Model):
    _name = 'todo.category'
    _description = '分类'

    name = fields.Char(u'名称')
    task_ids = fields.One2many('todo.task', 'category_id', string=u'待办事项')
    count = fields.Integer(u'任务数量', compute='_compute_task_count')

    @api.depends('task_ids')
    @api.multi
    def _compute_task_count(self):
        for record in self:
            record.count = len(record.task_ids)

