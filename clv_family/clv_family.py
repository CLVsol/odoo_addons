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
from datetime import datetime
from dateutil.relativedelta import relativedelta

class clv_family(models.Model):
    _name = 'clv_family'

    name = fields.Char('Name', required=True, size=64)
    alias = fields.Char('Alias', size=64, help='Common name that the Family is referred')
    code = fields.Char(size=64, string='Family Code', required=False)
    address_id = fields.Many2one('res.partner', 'Family Address', ondelete='restrict')
    family_phone = fields.Char('Family Phone', size=32)
    mobile_phone = fields.Char('Family Mobile', size=32)
    family_email = fields.Char('Family Email', size=240)
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Datetime("Inclusion Date", required=False, readonly=False,
                                     default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the family without removing it.",
                            default=1)

    _order='name'

    _sql_constraints = [('family_code_uniq', 'unique(code)', u'Error! The Family Code must be unique!')]

    @api.onchange('name')
    def _onchange_name(self):
        if not self.alias:
            self.alias = self.name

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
            return {'value': {'family_phone': address.phone, 'mobile_phone': address.mobile, 'family_email': address.email}}
        return {'value': {}}
