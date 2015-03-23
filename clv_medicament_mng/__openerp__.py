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
    'name': 'Medicament Management',
    'version': '1.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'description': '''
Medicament Management
=====================
    ''',
    'images': [],
    'depends': [
        'clv_base',
        'clv_tag',
        'clv_annotation',
        'clv_medicament',
        ],
    'data': [
        'security/clv_medicament_mng_security.xml',
        'security/ir.model.access.csv',
        'clv_medicament_mng_view.xml',
        'clv_tag/clv_tag_view.xml',
        'clv_annotation/clv_annotation_view.xml',
        'wkf/clv_medicament_mng_workflow.xml',
        'wkf/clv_medicament_mng_wkf_view.xml',
        'history/clv_medicament_mng_history_view.xml',
        'clv_medicament/clv_medicament_view.xml',
        'clv_medicament/clv_medicament_category_view.xml',
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
