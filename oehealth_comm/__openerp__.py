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
    'name': 'OeHealth: Community',
    'version': '1.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://CLVsol.net',
    'description': '''
    ''',
    'images': [
        #'images/oecomm_department.jpeg',
        #'images/oecomm_person.jpeg',
        #'images/oecomm_job_position.jpeg',
        #'static/src/img/community_image.png',
        #'static/src/img/company_image.png',
        #'static/src/img/default_image.png',
    ],
    'depends': [
                'oehealth',
                ]
                ,
    'data': [
             'security/ir.model.access.csv',
             #'board_oecomm_view.xml',
             #'oecomm_department_view.xml',
             #'process/oecomm_process.xml',
             #'oecomm_installer.xml',
             #'res_config_view.xml',
             #'',
             ],
    #'demo': ['oecomm_demo.xml'],
    'test': [
             #'test/open2recruit2close_job.yml',
             #'test/oecomm_demo.yml',
             ],
    'init_xml': [
                 'security/oehealth_comm_security.xml',
                 'res_partner_view.xml',
                 'oehealth_comm_view.xml',
                 'oehealth_comm_area/oehealth_comm_area_view.xml',
                 'oehealth_family/oehealth_family_view.xml',
                 'oehealth_person_code/oehealth_person_code_view.xml',
                 #'oecomm_person_role/oecomm_person_role_view.xml',
                 'oehealth_person/oehealth_person_view.xml',
                 'oehealth_person_category/oehealth_person_category_view.xml',
                 'oehealth_family_member_role/oehealth_family_member_role_view.xml',
                 'oehealth_family_member/oehealth_family_member_view.xml',
                 ],
    'test': [],
    'update_xml': [],
    'installable': True,
    'active': False,
    'css': [
            'static/src/css/oehealth.css',
             ],
}
