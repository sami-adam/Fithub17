from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductProduct(models.Model):
    _inherit = 'product.template'

    is_subscription_type = fields.Boolean(string='Subscription Product')
    period_type = fields.Selection([
        ('day', 'Day'),
        ('week', 'Week'),
        ('month', 'Month'),
        ('year', 'Year')
    ], default='month', string='Period Type')


class ProductCategory(models.Model):
    _inherit = 'product.category'

    is_subscription_category = fields.Boolean(string='Subscription Category')