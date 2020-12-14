from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = "account.move"

    self_id = fields.Many2one(
        comodel_name="account.move",
        compute="_get_self_id",
    )
    third_parties = fields.Float()
    net_total_amount = fields.Float(
        compute="_get_net_total_amount",
        store=True,
    )

    @api.depends("third_parties", "amount_untaxed")
    def _get_net_total_amount(self):
        for record in self:
            record.net_total_amount = record.amount_untaxed - record.third_parties

    def _get_self_id(self):
        for record in self:
            record.self_id = self.browse(record.id)
