# -*- coding: utf-8 -*-
from openerp import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    validator = fields.Many2one(
        readonly=False,

    )
    partner_attn_id = fields.Many2one(
        'res.partner',
        string='ATTN.',
        readonly=True,
        states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}
    )

    @api.multi
    def write(self, vals):
        is_confirmed_state = \
            vals.get('state', False) == 'confirmed' and \
            vals.get('validator', False)
        if is_confirmed_state:
            vals.update({'validator': self[0].validator.id})
        return super(PurchaseOrder, self).write(vals)
