from odoo import fields, models, api
from odoo.exceptions import UserError

class product(models.Model):
    _inherit = "product.template"

    state = fields.Selection([
        ('draft','Draft'),
        ('confirm', 'Confirm'),
        ('approve','Approve'),
    ],string='Status', readonly=True, default='draft')

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_approve(self):
        for rec in self:
            rec.state = 'approve'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            if self.search([('name', '=', rec.name),
                            ('id', '!=', rec.id)]):
                raise UserError('Sorry, This Product already exists !')

class purchase(models.Model):
    _inherit = "purchase.order"