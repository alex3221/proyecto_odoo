# -*- coding: utf-8 -*-
from odoo import http

# class ProyectoFinal(http.Controller):
#     @http.route('/proyecto_final/proyecto_final/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto_final/proyecto_final/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto_final.listing', {
#             'root': '/proyecto_final/proyecto_final',
#             'objects': http.request.env['proyecto_final.proyecto_final'].search([]),
#         })

#     @http.route('/proyecto_final/proyecto_final/objects/<model("proyecto_final.proyecto_final"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto_final.object', {
#             'object': obj
#         })