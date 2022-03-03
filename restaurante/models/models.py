# -*- coding: utf-8 -*-

from odoo import models, fields, api


class plato(models.Model):
     _name = 'restaurante.plato'
     _description = 'Plato del restaurante'

     name = fields.Char(string="Título", required=True)
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
