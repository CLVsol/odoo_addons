# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-TODAY OpenERP S.A. <http://www.openerp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Survey',
    'version': '1.0',
    'category': 'Tools',
    'description': """
This module is used for surveying.
==================================

It depends on the answers or reviews of some questions by different users. A
survey may have multiple pages. Each page may contain multiple questions and each
question may have multiple answers. Different users may give different answers of
question and according to that survey is done. Partners are also sent mails with
user name and password for the invitation of the survey.
    """,
    'author': 'OpenERP SA',
    'depends': [
    	'mail',
        'clv_patient',
        'clv_family',
    	],
    'data': [
        'clv_survey_report.xml',
        #'clv_survey_data.xml',
        'wizard/clv_survey_selection.xml',
        'wizard/clv_survey_answer.xml',
        'security/clv_survey_security.xml',
        'security/ir.model.access.csv',
        'clv_survey_view.xml',
        'wizard/clv_survey_print_statistics.xml',
        'wizard/clv_survey_print_answer.xml',
        'wizard/clv_survey_browse_answer.xml',
        'wizard/clv_survey_print.xml',
        'wizard/clv_survey_send_invitation.xml',
        'clv_survey_response_view.xml',
	    'clv_survey_view2.xml',
	    'clv_survey_request_view.xml',
        'clv_patient_view.xml',
        'clv_family_view.xml',
        ],
    'demo': [
        'clv_survey_demo.xml'
        ],
    'test': [
        'test/draft2open2close_clv_survey.yml',
        'test/draft2open2close_request.yml',
        'test/clv_survey_question_type.yml',
        'test/clv_survey_report.yml',
        ],
    'installable': True,
    'auto_install': False,
    'images': [
        'images/clv_survey_answers.jpeg',
        'images/clv_survey_pages.jpeg',
        'images/clv_surveys.jpeg',
        ],   
    'css': [
        'static/src/css/clv_survey.css',
        'static/css/clv_survey.css',
        ],
}
