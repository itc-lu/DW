from odoo import api, models, fields

class ProductProduct(models.Model):
    _name = "product.product"
    _inherit = "product.product"

    vendor_product_name = fields.Char(string="Vendor Product Name", compute="_compute_vendor")
    vendor_product_code = fields.Char(string="Vendor Product Code", compute="_compute_vendor")
    vendor_id = fields.Many2one(comodel_name="res.partner", string="Vendor", compute="_compute_vendor")

    qty_location_32 = fields.Float(string="Qty Divew/Stock", compute="_compute_stock")
    qty_location_37 = fields.Float(string="Qty Divew/Stock/Reserve", compute="_compute_stock")

    def _compute_vendor(self):
        for product in self:
            supplier_info = self.env["product.supplierinfo"].search([("product_id", "=", product.id)], limit=1)
            if not supplier_info:
                supplier_info = self.env["product.supplierinfo"].search([("product_tmpl_id", "=", product.product_tmpl_id.id)], limit=1)
            if supplier_info:
                product.vendor_id = supplier_info.name.id
                product.vendor_product_code = supplier_info.product_code
                product.vendor_product_name = supplier_info.product_name
            else:
                product.vendor_id = False
                product.vendor_product_code = ""
                product.vendor_product_name = ""

    def _compute_stock(self):
        for product in self:
            qty_32 = self.env["stock.quant"].search([("location_id", "=", 32), ("product_id", "=", product.id)])
            qty_37 = self.env["stock.quant"].search([("location_id", "=", 37), ("product_id", "=", product.id)])
            if qty_32:
                product.qty_location_32 = qty_32.quantity
            else:
                product.qty_location_32 = 0
            if qty_37:
                product.qty_location_37 = qty_37.quantity
            else:
                product.qty_location_37 = 0
