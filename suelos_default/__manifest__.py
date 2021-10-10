# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2021  jeo Software  (http://www.jeo-soft.com.ar)
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
    'name': 'suelos13',
    'version': '13.0.1.0.0',
    'category': 'Tools',
    'summary': 'Proyecto Suelos',
    'author': 'jeo Software',
    'depends': [
        'standard_depends_ce',
		
		'sale',
        'sale_management',
        'purchase',
		
        'stock',
        'product_in_box',
		
		#Contabilidad
        'account',
		'account_ux',
		'account_financial_report',

		
		#Localización
        'l10n_ar',
        'l10n_ar_ux',
        'l10n_ar_afipws',
        'l10n_ar_afipws_fe',
        'l10n_ar_bank',
        'l10n_ar_sale',
        'l10n_ar_account_withholding',
        'l10n_latam_invoice_document',
        'l10n_ar_reports',
        'l10n_ar_aeroo_base',
		'padron_afip',

    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'env-ver': '2',
    'odoo-license': 'CE',
    'port': '8069',

    'config': [
        'max_cron_threads = 1',
    ],

    'git-repos': [
        'git@github.com:jobiols/cl-suelos.git',
        'https://github.com/jobiols/odoo-jeo-ce.git',

		# Odoomates
		#==========================================================================================
        'https://github.com/odoomates/odooapps odoomates-odooapps',

        # Gabriela Rivero
		#==========================================================================================
        'https://github.com/regaby/odoo-custom regaby-odoo-custom',
		
        # todos juntos
		#==========================================================================================
        # 'https://github.com/OCA/account-closing oca-account-closing',
        'https://github.com/OCA/account-financial-reporting oca-account-financial-reporting', # noqa
        'https://github.com/OCA/account-financial-tools oca-account-financial-tools',
        'https://github.com/OCA/account-payment oca-account-payment',
        # 'https://github.com/OCA/apps-store oca-apps-store',
        # 'https://github.com/OCA/bank-payment oca-bank-payment',
        # 'https://github.com/OCA/business-requirement oca-business-requirement',
        # 'https://github.com/OCA/commission oca-commission',
        # 'https://github.com/OCA/contract oca-contract',
        # 'https://github.com/OCA/credit-control oca-credit-control',
        # 'https://github.com/OCA/crm oca-crm',
        # 'https://github.com/OCA/currency oca-currency',
        # 'https://github.com/OCA/ddmrp oca-ddmrp',
        # 'https://github.com/OCA/delivery-carrier oca-delivery-carrier',
        # 'https://github.com/OCA/e-commerce oca-e-commerce',
        # 'https://github.com/OCA/event oca-event',
        # 'https://github.com/OCA/field-service oca-field-service',
        # 'https://github.com/OCA/geospatial oca-geospatial',
        # 'https://github.com/OCA/hr oca-hr',
        # 'https://github.com/OCA/hr-timesheet oca-hr-timesheet',
        # 'https://github.com/OCA/knowledge oca-knowledge',
        # 'https://github.com/OCA/management-system oca-management-system',
        # 'https://github.com/OCA/manufacture oca-manufacture',
        # 'https://github.com/OCA/manufacture-reporting oca-manufacture-reporting',
        # 'https://github.com/OCA/margin-analysis oca-margin-analysis',
        # 'https://github.com/OCA/multi-company oca-multi-company',
        # 'https://github.com/OCA/oca-custom oca-oca-custom',
        # 'https://github.com/OCA/operating-unit oca-operating-unit',
        # 'https://github.com/OCA/partner-contact oca-partner-contact',
        # 'https://github.com/OCA/pos oca-pos',
        # 'https://github.com/OCA/product-attribute oca-product-attribute',
        # 'https://github.com/OCA/product-pack oca-product-pack',
        # 'https://github.com/OCA/project oca-project',
        # 'https://github.com/OCA/project-reporting oca-project-reporting',
        # 'https://github.com/OCA/purchase-workflow oca-purchase-workflow',
        # 'https://github.com/OCA/queue oca-queue',
        # 'https://github.com/OCA/report-print-send oca-report-print-send',
        'https://github.com/OCA/reporting-engine oca-reporting-engine',
        # 'https://github.com/OCA/sale-reporting oca-sale-reporting',
        'https://github.com/OCA/sale-workflow oca-sale-workflow',
        # 'https://github.com/OCA/server-auth oca-server-auth',
        # 'https://github.com/OCA/server-backend oca-server-backend',
        'https://github.com/OCA/server-tools oca-server-tools',
        'https://github.com/OCA/server-ux oca-server-ux',
        # 'https://github.com/OCA/social oca-social',
        # 'https://github.com/OCA/stock-logistics-barcode oca-stock-logistics-barcode',
        # 'https://github.com/OCA/stock-logistics-reporting oca-stock-logistics-reporting', # noqa
        # 'https://github.com/OCA/stock-logistics-transport oca-stock-logistics-transport', # noqa
        # 'https://github.com/OCA/stock-logistics-warehouse oca-stock-logistics-warehouse', # noqa
        # 'https://github.com/OCA/stock-logistics-workflow oca-stock-logistics-workflow',
        # 'https://github.com/OCA/timesheet oca-timesheet',
        # 'https://github.com/OCA/vertical-association oca-vertical-association',
        'https://github.com/OCA/web oca-web',
        # 'https://github.com/OCA/website oca-website',
        # 'https://github.com/OCA/bank-payment oca-bank-payment',
        # 'https://github.com/OCA/account-analytic',
        # 'https://github.com/ingadhoc/account-analytic ingadhoc-account-analytic',
        'https://github.com/ingadhoc/account-financial-tools ingadhoc-account-financial-tools', # noqa
        'https://github.com/ingadhoc/account-payment ingadhoc-account-payment',
        'https://github.com/ingadhoc/aeroo_reports ingadhoc-aeroo_reports',
        'https://github.com/ingadhoc/argentina-reporting ingadhoc-argentina-reporting',
        'https://github.com/ingadhoc/argentina-sale ingadhoc-argentina-sale',
        # 'https://github.com/ingadhoc/hr ingadhoc-hr',
        'https://github.com/ingadhoc/miscellaneous ingadhoc-miscellaneous',
        # 'https://github.com/ingadhoc/multi-company ingadhoc-multi-company',
        # 'https://github.com/ingadhoc/multi-store ingadhoc-multi-store',

        # Fix porque falla la instalacion de l10n_ar_ux
        'https://github.com/ingadhoc/odoo-argentina ingadhoc-odoo-argentina',

        #'https://github.com/jobiols/odoo-argentina jobiols-odoo-argentina',

        'https://github.com/ingadhoc/odoo-argentina-ce ingadhoc-odoo-argentina-ce',
        # 'https://github.com/ingadhoc/partner ingadhoc-partner',
        'https://github.com/ingadhoc/product ingadhoc-product',
        # 'https://github.com/ingadhoc/project ingadhoc-project',
        # 'https://github.com/ingadhoc/purchase ingadhoc-purchase',
        'https://github.com/ingadhoc/reporting-engine ingadhoc-reporting-engine',
        'https://github.com/ingadhoc/sale ingadhoc-sale',
        'https://github.com/ingadhoc/stock ingadhoc-stock',
        # 'https://github.com/ingadhoc/website ingadhoc-website',
    ],
    'docker-images': [
        'odoo jobiols/odoo-jeo:13.0',
        'postgres postgres:10.1-alpine',
    ]
}
