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
    'name': 'Person Management',
    'version': '1.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'description': '''
Person Management
=================
    ''',
    'images': [],
    'depends': [
        'clv_base',
        'clv_tag',
        'clv_annotation',
        'clv_address',
        'clv_person',
        'clv_patient',
        ],
    'data': [
        'security/clv_person_mng_security.xml',
        'security/ir.model.access.csv',
        'clv_person_mng_view.xml',
        # 'category/clv_person_category_view.xml',
        'clv_tag/clv_tag_view.xml',
        # 'clv_annotation/clv_annotation_view.xml',
        'wkf/clv_person_mng_workflow.xml',
        'wkf/clv_person_mng_wkf_view.xml',
        'history/clv_person_mng_history_view.xml',
        'menu/clv_person_mng_menu_view.xml',
        # 'clv_insurance/clv_insurance_view.xml',
        # 'clv_insurance_client/clv_insurance_client_view.xml',
        # 'role/clv_person_view.xml',
        'address/clv_person_mng_view.xml',
        # 'clv_patient/clv_person_mng_view.xml',
        # 'relation/clv_person_mng_relation_view.xml',
        'clv_person/clv_person_view.xml',
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
