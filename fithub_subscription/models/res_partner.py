from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_member = fields.Boolean(string='Is Member')
    identification_numer = fields.Char("ID")
    subscriptions_count = fields.Integer("Subscriptions", compute='_get_subscriptions_count')

    def _get_subscriptions_count(self):
        for rec in self:
            rec.subscriptions_count = 1

    def action_open_subscriptions(self):
        return