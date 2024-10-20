from odoo import models, fields


class estate_property_tag(models.Model):
    _name = "estate.property.tag"
    _description = "the tags of a property"
    name = fields.Char("name", required=True)
