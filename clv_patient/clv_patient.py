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

class clv_patient(osv.osv):
    _name = 'clv_patient'
    _inherits={
               'clv_person': 'person',
               }

    _columns = {
        'person': fields.many2one('clv_person', 'Related Person', required=True,
                                  ondelete='restrict', help='Person-related data of the patient'),
        #we need a related field in order to be able to sort the patient by name
        'name_related': fields.related('person', 'name', type='char', string='Related Person', 
                                       readonly=True, store=True),
        'patient_code': fields.char(size=64, string='Patient Code', required=False),
        'patient_date_inclusion':  fields.datetime("Inclusion Date", required=False, readonly=False),
        'active': fields.boolean('Active', 
                                 help="If unchecked, it will allow you to hide the patient without removing it."),
    }

    _order='name_related'

    _sql_constraints = [('patient_code_uniq', 'unique(patient_code)', u'Error! The Patient Code must be unique!')]

    _defaults = {
        'patient_date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': 1,
    }
    