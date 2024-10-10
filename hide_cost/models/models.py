# -*- coding: utf-8 -*-

from odoo import api,fields,models,_

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    margin = fields.Float(
        "Margin", compute='_compute_margin',
        digits='Product Price', store=True, groups="hide_cost.group_manager_cost", precompute=True)
    margin_percent = fields.Float(
        "Margin (%)", compute='_compute_margin', store=True, groups="hide_cost.group_manager_cost", precompute=True)
    purchase_price = fields.Float(
        string='Cost', compute="_compute_purchase_price",
        digits='Product Price', store=True, readonly=False, precompute=True,
        groups="hide_cost.group_manager_cost")
        
class SaleOrder(models.Model):
    _inherit = "sale.order"

    margin = fields.Monetary("Margin", groups="hide_cost.group_manager_cost", compute='_compute_margin', store=True)
    margin_percent = fields.Float("Margin (%)", groups="hide_cost.group_manager_cost", compute='_compute_margin', store=True, group_operator="avg")

class SaleReport(models.Model):
    _inherit = 'sale.report'

    margin = fields.Float('Margin', groups="hide_cost.group_manager_cost")
