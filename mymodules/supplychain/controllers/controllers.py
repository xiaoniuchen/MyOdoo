# -*- coding: utf-8 -*-
from odoo import http

# class Supplychain(http.Controller):
#     @http.route('/supplychain/supplychain/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/supplychain/supplychain/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('supplychain.listing', {
#             'root': '/supplychain/supplychain',
#             'objects': http.request.env['supplychain.supplychain'].search([]),
#         })

#     @http.route('/supplychain/supplychain/objects/<model("supplychain.supplychain"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('supplychain.object', {
#             'object': obj
#         })