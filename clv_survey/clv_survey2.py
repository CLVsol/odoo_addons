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

from osv import fields, osv

class clv_survey(osv.osv):
    _inherit = "clv_survey"
    _name = 'clv_survey'

    _columns = {
        'is_health_clv_survey' : fields.boolean('Is a Health Survey', help="Check if the survey is a Health Survey"),
        #'response_patient': fields.integer('Maximum Answer per Patient',
        #                                   help="Set to one if  you require only one Answer per patient"),
        #'patients': fields.many2many('clv_patient', 'clv_survey_persons_rel', 'clv_survey_id', 'patient_id', 'Patients'),
        #'invited_patient_ids': fields.many2many('clv_patient', 'clv_survey_invited_patient_rel', 'clv_survey_id', 'patient_id', 'Invited Patient'),
    }
    _defaults = {
        #'send_response': lambda * a: 1,
        'response_user': lambda * a:0,
        #'response_patient': lambda * a:1,
    }

class clv_survey_request(osv.osv):
    _inherit = "clv_survey.request"
    _name = "clv_survey.request"

    _columns = {
        'patient_id': fields.many2one("clv_patient", "Patient"),
    }

class clv_survey_response(osv.osv):
    _inherit = "clv_survey.response"
    _name = "clv_survey.response"
    _columns = {
        'patient_id' : fields.many2one('clv_patient', 'Patient'),
    }

    def name_get(self, cr, uid, ids, context=None):
        if not len(ids):
            return []
        reads = self.read(cr, uid, ids, ['user_id','date_create','patient_id'], context=context)
        res = []
        for record in reads:
            #name = (record['user_id'] and record['user_id'][1] or '' )+ ' (' + record['date_create'].split('.')[0] + ')'
            name = (record['patient_id'] and record['patient_id'][1] or '' ) + ' - ' + (record['user_id'] and record['user_id'][1] or '' ) + ' (' + record['date_create'].split('.')[0] + ')'
            res.append((record['id'], name))
        return res

class clv_survey_history(osv.osv):
    _inherit = "clv_survey.history"
    _name = 'clv_survey.history'
    _columns = {
        #'patient_id' : fields.many2one('clv_patient', 'Patient', readonly=True),
    }
