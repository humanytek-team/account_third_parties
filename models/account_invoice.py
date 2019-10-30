# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    third_parties = fields.Float(
    )
    net_total_amount = fields.Float(
        compute='_get_net_total_amount',
    )

    @api.depends('third_parties', 'amount_untaxed_invoice_signed')
    def _get_net_total_amount(self):
        for record in self:
            record.net_total_amount = record.amount_untaxed_invoice_signed - record.third_parties
