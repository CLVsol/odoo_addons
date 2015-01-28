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
    'name': 'CLVagro - the CLVsol agro solution',
    'version': '1.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://clvsol.com',
    'description': '''
the CLVsol agro solution
------------------------
This module will install all the necessary modules to implement the CLVsol agro solution.
    ''',
    'depends': [
        'clv_base',
        'clv_tag',
        'clv_annotation',
        'clv_place',
        'clv_frame',
        'clv_tray',
        'clv_batch',
        'clv_seedling',
        ],
    'data': [
        'clvagro_view.xml',
        'seq/clv_tag_sequence.xml',
        'seq/clv_annotation_sequence.xml',
        'seq/clv_annotation_category_sequence.xml',
        'seq/clv_place_sequence.xml',
        'seq/clv_place_category_sequence.xml',
        'seq/clv_frame_sequence.xml',
        'seq/clv_frame_category_sequence.xml',
        'seq/clv_tray_sequence.xml',
        'seq/clv_tray_category_sequence.xml',
        'seq/clv_batch_sequence.xml',
        'seq/clv_batch_category_sequence.xml',
        ],
    'test': [],
    'installable': True,
    'active': False,
}
