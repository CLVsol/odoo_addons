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

from osv import osv
from osv import fields

class oehealth_pbm_insured(osv.Model):
    _name='oehealth.pbm.insured'
    _inherits={
               'res.partner': 'partner_id',
               }
    
    _columns={
        'partner_id': fields.many2one('res.partner', 'Related Partner', required=True,
                                     ondelete='cascade', help='Partner-related data of the insured'),
        #we need a related field in order to be able to sort the person by name
        'name_related': fields.related('partner_id', 'name', type='char', string='Related Partiner', 
                                       readonly=True, store=True),
        'insured_code': fields.many2one('oehealth.pbm.insured.code', 'Insured Code'),
        'plan_id': fields.many2one('oehealth.pbm.plan', string='PBM Plan',  
                                   help='Pharmaceutic Benefit Management plan'),
        'patient_id':fields.many2one('oehealth.patient', 'Related Patient'),
        'general_info': fields.text(string='General Information',
                                    help='General information about the insured'),
    }

    _order='name_related'

    _sql_constraints = [
                        ('insured_code_uniq', 'unique(insured_code)', 'Insured code already in use!'),
                        ]
