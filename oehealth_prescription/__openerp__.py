# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2012  Carlos Eduardo Vercelino - CLVsol                        #
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
    'name': 'OeHealth: Prescription',
    'version': '1.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://CLVsol.net',
    'description': '''
    ''',
    'images': [],
    'depends': [
                'oehealth',
                'oehealth_medicament',
                ]
                ,
    'data': [
             'security/ir.model.access.csv',
             ],
    'demo': [],
    'test': [],
    'init_xml': [
                 'security/oehealth_prescription_security.xml',
                 'oehealth_prescription_view.xml',
                 'oehealth_drug_form/oehealth_drug_form_view.xml',
                 'oehealth_drug_route/oehealth_drug_route_view.xml',
                 'oehealth_medication_dosage/oehealth_medication_dosage_view.xml',
                 'oehealth_medication_template/oehealth_medication_template_view.xml',
                 'oehealth_prescription_line/oehealth_prescription_line_view.xml',
                 'oehealth_prescription_order/oehealth_prescription_order_view.xml',
                 'oehealth_patient_medication/oehealth_patient_medication_view.xml'
                 ],
    'test': [],
    'update_xml': [],
    'installable': True,
    'active': False,
    'css': [],
}
