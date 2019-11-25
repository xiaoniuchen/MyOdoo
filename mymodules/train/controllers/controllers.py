# -*- coding: utf-8 -*-
from odoo import http

# class Train(http.Controller):
#     @http.route('/train/train/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/train/train/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('train.listing', {
#             'root': '/train/train',
#             'objects': http.request.env['train.train'].search([]),
#         })

#     @http.route('/train/train/objects/<model("train.train"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('train.object', {
#             'object': obj
#         })