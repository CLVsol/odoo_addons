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
    'name': 'OeHealth: Health Survey',
    'version': '1.0.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'website': 'http://CLVsol.net',
    'description': '''
    ''',
    'depends': [
                'oehealth',
                'oehealth_patient',
                'survey',
                ]
                ,
    'data': [
             #'security/ir.model.access.csv',
             ],
    'init_xml': [
                 'security/oehealth_survey_security.xml',
                 'survey_view.xml',
                 'survey_response_view.xml',
                 'oehealth_patient_view.xml',
                 'survey_request_view.xml',
                 #'oecomm_survey_report.xml',
                 #'wizard/oecomm_survey_answer.xml',
                 #'survey_request_view.xml',
                ],
    'test': [],
    'update_xml': [],
    'installable': True,
    'active': False,

#    'depends': ['mail'],
#    'data': [
#        'survey_report.xml',
#        'survey_data.xml',
#        'wizard/survey_selection.xml',
#        'wizard/survey_answer.xml',
#        'security/survey_security.xml',
#        'security/ir.model.access.csv',
#        'survey_view.xml',
#        'wizard/survey_print_statistics.xml',
#        'wizard/survey_print_answer.xml',
#        'wizard/survey_browse_answer.xml',
#        'wizard/survey_print.xml',
#        'wizard/survey_send_invitation.xml'
#    ],
#    'demo': ['survey_demo.xml'],
#    'test': [
#        'test/draft2open2close_survey.yml',
#        'test/draft2open2close_request.yml',
#        'test/survey_question_type.yml',
#        'test/survey_report.yml',
#    ],
#    'installable': True,
#    'auto_install': False,
#    'images': ['images/survey_answers.jpeg','images/survey_pages.jpeg','images/surveys.jpeg'],   
#    'css': ['static/src/css/survey.css','static/css/survey.css'],
}
