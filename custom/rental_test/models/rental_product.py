from odoo import models, fields

class RentalProduct(models.Model):
   _name = "rental.product"
   _description = "Rental Product model"

   name = fields.Char(string="Name")
   Category = fields.Char(string="Categoy")