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
        'family_name': fields.char('Name', required=True, size=64),
        'family_alias': fields.char('Alias', size=64, help='Common name that the Family is referred'),
        'family_code': fields.char(size=64, string='Family Code', required=False),
        'family_address_id': fields.many2one('res.partner', 'Family Address', ondelete='restrict'),
        'family_phone': fields.char('Family Phone', size=32),
        'family_mobile_phone': fields.char('Family Mobile', size=32),
        'family_email': fields.char('Family Email', size=240),
        'family_notes':  fields.text(string='Notes'),

        'associate_family': fields.boolean('Associate Family', 
                                           help="If checked, it will require to associate to a family."),
        'family_id': fields.many2one('clv_family', 'Family', ondelete='restrict'),
        'family_uid_inclusion': fields.many2one('res.users', 'Inclusion User', required=False, readonly=False),
        'family_date_inclusion': fields.datetime("Inclusion Date", required=False, readonly=False),
        'family_date_activation': fields.datetime("Activation date", required=False, readonly=False),
        'family_date_inactivation': fields.datetime("Inactivation date", required=False, readonly=False),
        'family_date_suspension': fields.datetime("Suspension date", required=False, readonly=False),
        'family_state': fields.selection([('new','New'),
                                          ('active','Active'),
                                          ('inactive','Inactive'),
                                          ('suspended','Suspended')
                                          ], string='Status', readonly=False, required=False, help=""),
        } 

    _defaults = {
        'associate_family': 0,
        'family_uid_inclusion': lambda obj,cr,uid,context: uid,
        'family_date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
    
    _sql_constraints = [('family_code_uniq', 'unique(family_code)', u'Error! The Family Code must be unique!')]
