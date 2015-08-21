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
    'name': 'Medicament Dispensation Management for CLVhealth BioBox',
    'version': '1.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'description': '''
Medicament Dispensation Management for CLVhealth BioBox
=======================================================
    ''',
    'images': [],
    'depends': [
        # 'clv_base',
        # 'clv_tag',
        # 'clv_annotation',
        # 'clv_medicament',
        # 'clv_pharmacy',
        # 'clv_professional',
        # 'clv_insured_card',
        'clv_medicament_dispensation',
        ],
    'data': [
        'security/clv_medicament_dispensation_mng_security.xml',
        'security/ir.model.access.csv',
        'clv_medicament_dispensation_mng_view.xml',
        # 'category/clv_medicament_dispensation_mng_category_view.xml',
        # 'clv_tag/clv_tag_view.xml',
        # 'clv_annotation/clv_annotation_view.xml',
        # 'seq/clv_medicament_dispensation_mng_sequence.xml',
        # 'seq/clv_medicament_dispensation_mng_category_sequence.xml',
        # 'wkf/clv_medicament_dispensation_mng_workflow.xml',
        # 'wkf/clv_medicament_dispensation_mng_wkf_view.xml',
        # 'history/clv_medicament_dispensation_mng_history_view.xml',
        # 'clv_medicament_template/clv_medicament_template_view.xml',
        'menu/clv_medicament_dispensation_mng_menu_view.xml',
        'clv_pharmacy/clv_pharmacy_view.xml',
        'clv_professional/clv_professional_view.xml',
        'clv_insured_card/clv_insured_card_view.xml',
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
