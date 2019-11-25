# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
from odoo import tools, _
from odoo.modules.module import get_module_resource

class supplier(models.Model):
    _name = 'supplychain.supplier'
    _description = 'supplychain.supplier'

    supplier_number = fields.Char(string='供应商编码', required=True)
    name = fields.Char(string='供应商名称')
    address = fields.Char(string='供应商地址')
    email = fields.Char(string='供应商邮箱')
    state = fields.Selection([
        ('N', '未审核'),
        ('Y', '已审核'),
    ], string='Status', readonly=True, index=True, copy=False, default='N')
    img = fields.Binary(compute='show_img', store=False)
    company_id = fields.Many2one('res.company', 'Company', required=True,invisible=False,
                                 default=lambda self: self.env.user.company_id.id)


    @api.multi
    def active_btn(self):
        return self.write({'state': 'Y'})

    @api.multi
    def draft_btn(self):
        return self.write({'state': 'N'})

    @api.model
    @api.depends('state')
    def show_img(self):
        if self.state == 'Y':
            image_path = get_module_resource('supplychain', 'static/img', 'active.png')
            self.img =  tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))
        if self.state == 'N':
            image_path = get_module_resource('supplychain', 'static/img', 'draft.png')
            self.img = tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))
