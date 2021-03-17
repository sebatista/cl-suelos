# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#    Copyright (C) 2017  jeo Software  (http://www.jeosoft.com.ar)
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
# -----------------------------------------------------------------------------

{
    'name': 'Vertical Ceramicas',
    'version': '8.0.1.3.0',
    'category': 'Tools',
    'summary': 'Customización mayorista de ceramicas',
    'author': 'jeo Software',
    'depends': [
        'product',
        'base',
        'account',
        'stock',
        'purchase',
        'stock_account', 'stock_voucher'
    ],
    'data': [
        'views/report_stockpicking.xml',
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'views/account_tax_view.xml',
        'stock_report.xml',
        'views/res_product.xml',
        'views/stock_view.xml',
        'views/res_config_view.xml'
    ],
    'test': [

    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [],
}
