# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
from odoo import tools, _
from odoo.modules.module import get_module_resource

class item(models.Model):
    _name = 'supplychain.item'
    _description = 'supplychain.item'

    item_number = fields.Char(string='物料编码', required=True)
    name = fields.Char(string='品名')
    specification = fields.Char(string='规格')
    type = fields.Char(string='类型')
    unit = fields.Selection([
        ('PCS', 'PCS'),
        ('KG', 'KG'),
        ('M', 'M'),
        ('M3', 'M3')
    ], default='PCS', string='单位')
    warehouse = fields.Char(string='主仓库')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
    ], string='Status', readonly=True, index=True, copy=False, default='draft')
    img = fields.Binary(compute='show_img', store=False)
    company_id = fields.Many2one('res.company', 'Company', required=True, default=lambda self: self.env.user.company_id.id)


    @api.multi
    def active_btn(self):
        return self.write({'state': 'active'})

    @api.multi
    def draft_btn(self):
        return self.write({'state': 'draft'})

    @api.model
    @api.depends('state')
    def show_img(self):
        if self.state == 'active':
            image_path = get_module_resource('supplychain', 'static/img', 'active.png')
            self.img =  tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))
        if self.state == 'draft':
            self.img = None
