from odoo import models, fields, api
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta


class offer(models.Model):
    _name = "estate.property.offer"
    price = fields.Float("Price")
    status = fields.Selection([("accepted", "Accepted"), ("refused", "Refused")], name="Status", copy=False)
    partner_id = fields.Many2one("res.partner", name="Buyer", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline", readonly=False)
    validity = fields.Integer(string="Validity (Days)", default=7, readonly=False)

    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = fields.Date.today() + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = record.date_deadline.toordinal() - fields.Date.today().toordinal()

    def action_accept_offer(self):
        for record in self:
            for offer in record.property_id.offer_ids:
                if offer.status == "accepted":
                    raise UserError("An offer has already been accepted")
            record.status = "accepted"
            record.property_id.selling_price = record.price
            record.property_id.buyer = record.partner_id
        return True

    def action_refuse_offer(self):
        for record in self:
            record.status = "refused"
        return True
