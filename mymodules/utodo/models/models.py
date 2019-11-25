# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TodoTask(models.Model):
    _inherit = 'todo.task'
    budget = fields.Float(string=u'预算')
    manager = fields.Many2many('res.users','res_user_todotask_rel','user_id','todotask_id','责任人')

    @api.onchange('is_done')
    def onchange_isdone(self):
        self.budget = 0