from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_member = fields.Boolean(string='Is Member')
    identification_numer = fields.Char("ID")
    subscriptions_count = fields.Integer("Subscriptions", compute='_get_subscriptions_count')

    def _get_subscriptions_count(self):
        for rec in self:
            rec.subscriptions_count = self.env['account.move'].search_count([('partner_id', '=', self.id),('is_subscription', '=', True)])

    def action_open_subscriptions(self):
        subscription_action = self.env.ref('fithub_subscription.action_fithub_subscription').read()[0]
        subscription_action['domain'] = [('partner_id', '=', self.id), ('is_subscription', '=', True)]
        subscription_action['context'] = {'default_partner_id': self.id, 'default_is_subscription': True}
        return subscription_action
