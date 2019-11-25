# -*- coding: utf-8 -*-
from odoo import http

# class Xksystem(http.Controller):
#     @http.route('/xksystem/xksystem/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xksystem/xksystem/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xksystem.listing', {
#             'root': '/xksystem/xksystem',
#             'objects': http.request.env['xksystem.xksystem'].search([]),
#         })

#     @http.route('/xksystem/xksystem/objects/<model("xksystem.xksystem"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xksystem.object', {
#             'object': obj
#         })