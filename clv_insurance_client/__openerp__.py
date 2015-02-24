# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

{
    'name': 'Insurance Client',
    'version': '1.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'description': '''
Insurance Client
================
    ''',
    'images': [],
    'depends': [
        'clv_base',
        'clv_tag',
        'clv_annotation',
        ],
    'data': [
        'security/clv_insurance_client_security.xml',
        'security/ir.model.access.csv',
        'clv_insurance_client_view.xml',
        'category/clv_insurance_client_category_view.xml',
        'clv_annotation/clv_annotation_view.xml',
        'clv_tag/clv_tag_view.xml',
        'seq/clv_insurance_client_sequence.xml',
        'seq/clv_insurance_client_category_sequence.xml',
        'wkf/clv_insurance_client_workflow.xml',
        'wkf/clv_insurance_client_wkf_view.xml',
        'history/clv_insurance_client_history_view.xml',
        'menu/clv_insurance_client_menu_view.xml'
        ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'active': False,
    'css': [],
}
