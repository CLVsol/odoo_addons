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
    'name': 'Lab Test',
    'version': '1.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'description': '''
Lab Test
========
    ''',
    'images': [],
    'depends': [
        # 'product',
        'clv_base',
        'clv_tag',
        'clv_annotation',
        'clv_patient',
        ],
    'data': [
        'security/clv_lab_test_security.xml',
        'security/ir.model.access.csv',
        'clv_lab_test_view.xml',
        # 'clv_patient_view.xml',
        # 'clv_person_view.xml',
        # 'category/clv_patient_category_view.xml',
        # 'clv_tag/clv_tag_view.xml',
        # 'clv_annotation/clv_annotation_view.xml',
        'seq/clv_lab_test_sequence.xml',
        # 'seq/clv_patient_category_sequence.xml',
        'wkf/clv_lab_test_workflow.xml',
        'wkf/clv_lab_test_wkf_view.xml',
        # 'history/clv_patient_history_view.xml',
        # 'clv_lab_test_workflow.xml',
        'clv_lab_test_unit_view.xml',
        'clv_lab_test_type_view.xml',
        'clv_lab_test_criterion_view.xml',
        'clv_lab_test_request_view.xml',
        'clv_patient/clv_patient_view.xml',
        'wizard/create_lab_test.xml',
        # 'clv_lab_test_outcome_view.xml',
        'lab_test_data.xml',
        'menu/clv_lab_test_menu_view.xml',
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
