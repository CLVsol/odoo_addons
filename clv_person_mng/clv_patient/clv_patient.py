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

from openerp.osv import fields, osv
from datetime import datetime

class clv_person_mng(osv.osv):
    _inherit = 'clv_person_mng'

    _columns = {
        'associate_patient': fields.boolean('Associate Patient', 
                                         help="If checked, it will require to associate to a patient."),
        'patient_code': fields.char(size=64, string='Patient Code', required=False),
        'patient_id': fields.many2one('clv_patient', 'Patient', ondelete='restrict'),
        'patient_uid_inclusion': fields.many2one('res.users', 'Inclusion User', required=False, readonly=False),
        'patient_date_inclusion': fields.datetime("Inclusion Date", required=False, readonly=False),
        'patient_date_activation': fields.datetime("Activation date", required=False, readonly=False),
        'patient_date_inactivation': fields.datetime("Inactivation date", required=False, readonly=False),
        'patient_date_suspension': fields.datetime("Suspension date", required=False, readonly=False),
        'patient_state': fields.selection([('new','New'),
                                           ('active','Active'),
                                           ('inactive','Inactive'),
                                           ('suspended','Suspended')
                                           ], string='Status', readonly=False, required=False, help=""),
        }

    _defaults = {
        'associate_patient': 0,
        'patient_uid_inclusion': lambda obj,cr,uid,context: uid,
        'patient_date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
    
    _sql_constraints = [('patient_code_uniq', 'unique(patient_code)', u'Error! The Patient Code must be unique!')]
