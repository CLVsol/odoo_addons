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
    'name': 'Place',
    'version': '1.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'description': '''
Place
=====
    ''',
    'depends': [
        'clv_base',
        'clv_tag',
        'clv_annotation',
        'clv_address',
        ],
    'data': [
        'security/clv_place_security.xml',
        'security/ir.model.access.csv',
        'clv_place_view.xml',
        'category/clv_place_category_view.xml',
        'clv_tag/clv_tag_view.xml',
        'clv_annotation/clv_annotation_view.xml',
        'seq/clv_place_seq_view.xml',
        'seq/clv_place_sequence.xml',
        'seq/clv_place_category_sequence.xml',
        'wkf/clv_place_workflow.xml',
        'wkf/clv_place_wkf_view.xml',
        'history/clv_place_history_view.xml',
        'menu/clv_place_menu_view.xml',
        ],
    'test': [],
    'installable': True,
    'active': False,
}
