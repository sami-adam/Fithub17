from odoo import models, fields, api, _
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_subscription = fields.Boolean('Subscription')
    subscription_end_date = fields.Date('Subscription End', compute='_get_subscription_end_date')


    @api.depends('invoice_line_ids.product_id', 'invoice_line_ids.quantity', 'invoice_date')
    def _get_subscription_end_date(self):
        for rec in self:
            if rec.is_subscription and rec.invoice_date:
                days, weeks, months, years = 0, 0, 0, 0
                for line in rec.invoice_line_ids:
                    if line.product_id.period_type == 'day':
                        days += line.quantity
                    if line.product_id.period_type == 'week':
                        weeks += line.quantity
                    if line.product_id.period_type == 'month':
                        months += line.quantity
                    if line.product_id.period_type == 'year':
                        years += line.quantity
                rec.subscription_end_date = rec.invoice_date + relativedelta(days=days, weeks=weeks, months=months, years=years)
            else:
                rec.subscription_end_date = False




