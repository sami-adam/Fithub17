# -*- coding: utf-8 -*-
# from odoo import http


# class FithubSubscription(http.Controller):
#     @http.route('/fithub_subscription/fithub_subscription', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fithub_subscription/fithub_subscription/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fithub_subscription.listing', {
#             'root': '/fithub_subscription/fithub_subscription',
#             'objects': http.request.env['fithub_subscription.fithub_subscription'].search([]),
#         })

#     @http.route('/fithub_subscription/fithub_subscription/objects/<model("fithub_subscription.fithub_subscription"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fithub_subscription.object', {
#             'object': obj
#         })

