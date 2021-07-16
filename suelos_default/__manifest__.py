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

    'git-repos': [
        'git@github.com:jobiols/cl-suelos.git',
    ],
    'docker-images': [
        'odoo jobiols/odoo-jeo:13.0',
        'postgres postgres:10.1-alpine',
    ]
}
