from odoo import models, fields


class estate_property_type(models.Model):
    _name = "estate.property.type"
    _description = "the types of property"
    name = fields.Char("name", required=True)
