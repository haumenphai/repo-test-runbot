# -*- coding: utf-8 -*-
# from odoo import http


# class SchooTest(http.Controller):
#     @http.route('/schoo_test/schoo_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/schoo_test/schoo_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('schoo_test.listing', {
#             'root': '/schoo_test/schoo_test',
#             'objects': http.request.env['schoo_test.schoo_test'].search([]),
#         })

#     @http.route('/schoo_test/schoo_test/objects/<model("schoo_test.schoo_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('schoo_test.object', {
#             'object': obj
#         })
