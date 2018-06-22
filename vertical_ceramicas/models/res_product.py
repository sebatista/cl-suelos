# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields, api
from openerp import SUPERUSER_ID
from openerp.exceptions import Warning
from lxml import etree


class ProductProduct(models.Model):
    _inherit = 'product.product'

    prod_in_box = fields.Float(
        u'Cant producto por caja',
        help=u'Cantidad de metros cuadrados o lineales que entran en una caja'
    )
    prod_in_box_uom = fields.Selection([
        ('na', 'No aplica'),
        ('mt2', 'mts cuadrados'),
        ('mt', 'mts'),
    ],
        'Unidad', required=True,
        default='mt2'
    )

    @api.one
    @api.constrains('prod_in_box', 'prod_in_box_uom', 'type')
    def _check_prod_in_box(self):
        if self.prod_in_box_uom == 'na' and self.prod_in_box - 0.0 > 0.001:
            raise Warning('Cantidad de producto por caja debe ser cero')

        if self.prod_in_box_uom != 'na' and self.type != 'product':
            raise Warning('Si aplica cantidad de producto por caja, '
                          'el tipo de producto debe ser almacenable')
