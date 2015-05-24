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

from openerp import models, fields, api
from datetime import *

class clv_pharmacy(models.Model):
    _name = 'clv_pharmacy'

    name = fields.Char('Pharmacy', required=True, size=64, translate=False)
    alias = fields.Char('Alias', size=64, help='Common name that the Pharmacy is referred')
    code = fields.Char(size=64, string='Pharmacy Code', required=False)
    address_id = fields.Many2one('clv_address', 'Client Address', ondelete='restrict')
    client_phone = fields.Char('Client Phone', size=32)
    mobile_phone = fields.Char('Client Mobile', size=32)
    client_email = fields.Char('Client Email', size=240)
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Date('Inclusion Date')
    active = fields.Boolean('Active', help="If unchecked, it will allow you to hide the insurance client without removing it.")

    _order='name'

    _sql_constraints = [('code_uniq', 'unique(code)', u'Error! The Pharmacy Code must be unique!')]

    _defaults = {
        'date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': 1,
        }

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('clv_address').browse(cr, uid, address, context=context)
            return {'value': {'client_phone': address.phone, 'mobile_phone': address.mobile, 'client_email': address.email}}
        return {'value': {}}
