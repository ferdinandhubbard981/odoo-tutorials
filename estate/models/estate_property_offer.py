from odoo import models, fields

class offer(models.Model):
    _name = "estate.property.offer"
    price = fields.Float("Price")
    status = fields.Selection([("accepted", "Accepted"), ("refused", "Refused")], name="Status", copy=False)
    partner_id = fields.Many2one("res.partner", name="Buyer", required=True)
    property_id = fields.Many2one("estate.property", required=True)
