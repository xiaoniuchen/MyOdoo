# -*- coding: utf-8 -*-
from odoo import http

# class Utodo(http.Controller):
#     @http.route('/utodo/utodo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/utodo/utodo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('utodo.listing', {
#             'root': '/utodo/utodo',
#             'objects': http.request.env['utodo.utodo'].search([]),
#         })

#     @http.route('/utodo/utodo/objects/<model("utodo.utodo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('utodo.object', {
#             'object': obj
#         })