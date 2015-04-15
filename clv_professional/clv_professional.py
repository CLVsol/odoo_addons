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

class clv_professional(models.Model):
    _name = 'clv_professional'

    name = fields.Char('Name', required=True, size=128)
    alias = fields.Char('Alias', size=64, help='Common name that the Professional is referred')
    code = fields.Char(size=64, string='Professional Code', required=False)
    address_id = fields.Many2one('res.partner', 'Professional Address', ondelete='restrict')
    professional_phone = fields.Char('Professional Phone', size=32)
    mobile_phone = fields.Char('Professional Mobile', size=32)
    professional_email = fields.Char('Professional Email', size=240)
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Datetime("Inclusion Date", required=False, readonly=False,
                                     default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the professional without removing it.",
                            default=1)
    professional_id = fields.Char(size=64, string='Professional ID', required=False)

    _order='name'

    _sql_constraints = [
        ('professional_code_uniq', 'unique(code)', u'Error! The Professional Code must be unique!'),
        ('professional_id_uniq', 'unique(professional_id)', u'Error! The Professional ID must be unique!'),
        ]

    @api.onchange('name')
    def _onchange_name(self):
        if not self.alias:
            self.alias = self.name

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
            return {'value': {'professional_phone': address.phone, 'mobile_phone': address.mobile, 'professional_email': address.email}}
        return {'value': {}}

    @api.multi
    @api.depends('name', 'professional_id')
    def name_get(self):
        result = []
        for clv_professional in self:
            if clv_professional.professional_id != False:
                result.append((clv_professional.id, '%s [%s]' % (clv_professional.name, clv_professional.professional_id)))
            else:
                result.append((clv_professional.id, '%s' % (clv_professional.name)))
        return result
