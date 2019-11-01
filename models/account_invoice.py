# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    self_id = fields.Many2one(
        comodel_name='account.invoice',
        compute='_get_self_id',
    )
    third_parties = fields.Float(
    )
    net_total_amount = fields.Float(
        compute='_get_net_total_amount',
        store=True,
    )
    amount_untaxed_invoice_signed = fields.Monetary(
        store=True,
    )
    amount_tax_signed = fields.Monetary(
        store=True,
    )

    @api.depends('third_parties', 'amount_untaxed_invoice_signed')
    def _get_net_total_amount(self):
        for record in self:
            record.net_total_amount = record.amount_untaxed_invoice_signed - record.third_parties

    def _get_self_id(self):
        for record in self:
            record.self_id = self.browse(record.id)
