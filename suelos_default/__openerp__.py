# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2016  jeo Software  (http://www.jeo-soft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------------
{
    'name': 'suelos',
    'version': '8.0.5.0.0',
    'category': 'Tools',
    'summary': 'Customización Suelos',
    'author': 'jeo Software',
    'depends': [
        'l10n_ar_base',  # modulo base para localización argentina
        'disable_openerp_online',  # elimina referencias a odoo online
        'account_cancel',  # permite cancelar asientos
        'hide_product_variants',  # oculta las variantes
        'invoice_order_by_id',  # ordena facturas ultima arriba
        #        'sale_order_recalculate_prices',  # agrega boton para recalcular precios
        #        'partner_search',            # permite buscar partners por varios criterios
        'account_journal_sequence',  # ordena diarios
        # 'account_statement_move_import'  # agrega boton de importar aputnes en extractos bancarios
        'l10n_ar_aeroo_sale',  # dependencia requerida
        'l10n_ar_aeroo_purchase',  # dependencia requerida
        'l10n_ar_aeroo_einvoice',  # dependencia requerida
        'l10n_ar_aeroo_stock',  # dependencia requerida
        'l10n_ar_aeroo_voucher',  # dependencia requerida
        #        'po_custom_reports',        # dependencia requerida
        #        'custom_vat_ledger',        # dependencia requerida
        #        'odoo_argentina_fix',       # patch a la localización
        'account_invoice_tax_wizard',  # agrega insercion manual de impuestos para factura de compras
        'product_unique_default_code',  # impide que se duplique el default_code
        'hide_messaging',  # oculta el menu de mensajeria
        'voucher_payment_check_fix',  # evita que aparezca cheques propios en medios de pago de cliente
        'account_invoice_tax_auto_update',  # autocalcula los impuestos al salvar asi no hay que hacer el update
        'server_mode',
        'account_clean_cancelled_invoice_number'
    ],
    'data': [
        'views/custom_reports.xml',
        'views/res_product.xml'
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'port': '8069',
    'repos': [
        {'usr': 'jobiols', 'repo': 'cl-suelos', 'branch': '8.0'},
        {'usr': 'jobiols', 'repo': 'odoo-jeo-ce', 'branch': '8.0'},
        {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.1'},
        {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '9.5'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'}
    ]
}
