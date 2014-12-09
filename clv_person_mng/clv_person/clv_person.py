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
from dateutil.relativedelta import relativedelta

class clv_person_mng(osv.osv):
    _inherit = 'clv_person_mng'

    _columns = {
        'person_code': fields.char(size=64, string='Person Code', required=False),
        'person_id': fields.many2one('clv_person', 'Person', ondelete='restrict'),
        'address_id': fields.many2one('res.partner', 'Person Address', ondelete='restrict'),
        'person_date_inclusion': fields.datetime("Inclusion Date", required=False, readonly=False),
        'person_phone_2': fields.char('Person Phone', size=32),
        'mobile_phone_2': fields.char('Person Mobile', size=32),
        'person_email_2': fields.char('Person Email', size=240),
        'person_date_activation': fields.datetime("Activation date", required=False, readonly=False),
        'person_date_inactivation': fields.datetime("Inactivation date", required=False, readonly=False),
        'person_date_suspension': fields.datetime("Suspension date", required=False, readonly=False),
        'person_state': fields.selection([('new','New'),
                                          ('active','Active'),
                                          ('inactive','Inactive'),
                                          ('suspended','Suspended')
                                          ], string='Status', readonly=True, required=True, help=""),
        }

    _defaults = {
        'person_date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
    
    _sql_constraints = [('person_code_uniq', 'unique(person_code)', u'Error! The Person Code must be unique!')]

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
            return {'value': {'person_phone_2': address.phone, 'mobile_phone_2': address.mobile, 'person_email_2': address.email}}
            return {'value': {}}
        return {'value': {}}
