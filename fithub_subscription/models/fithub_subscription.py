from odoo import models, fields, api, _
from odoo.exceptions import UserError


class FithubSubscription(models.Model):
    _name = 'fithub.subscription'
    _description = 'Fithub Subscription'

    name = fields.Char(string='Name', default=_('New'))
    description = fields.Text(string='Description')
    partner_id = fields.Many2one('res.partner', string='Member')
    product_category_id = fields.Many2one('product.category', string='Subscription Category')
    product_id = fields.Many2one('product.product', string='Subscription Plan')
    start_date = fields.Date(string='Start Date', default=fields.Date.today)
    end_date = fields.Date(string='End Date')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('paid', 'Paid'),
        ('active', 'Active'),
        ('expired', 'Expired'),
    ], string='Status', default='draft')

