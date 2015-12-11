# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).                        #
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

from openerp import api
from openerp.osv import osv, fields


class clv_person_mng(osv.Model):
    _inherit = 'clv_person_mng'

    _columns = {
        'addr_name': fields.char('Name', required=False, select=True),
        'addr_alias': fields.char('Alias', size=64, help='Common name that the Address is referred'),
        'addr_code': fields.char(size=64, string='Address Code'),
        'addr_notes': fields.text('Notes'),
        'addr_street': fields.char('Street'),
        'addr_street2': fields.char('Street2'),
        'addr_zip': fields.char('Zip', size=24, change_default=True),
        'addr_city': fields.char('City'),
        'addr_state_id': fields.many2one("res.country.state", 'State', ondelete='restrict'),
        'addr_country_id': fields.many2one('res.country', 'Country', ondelete='restrict'),
        'addr_email': fields.char('Email'),
        'addr_phone': fields.char('Phone'),
        'addr_fax': fields.char('Fax'),
        'addr_mobile': fields.char('Mobile'),
        }

    @api.multi
    def onchange_addr_state(self, addr_state_id):
        if addr_state_id:
            state = self.env['res.country.state'].browse(addr_state_id)
            return {'value': {'addr_country_id': state.country_id.id}}
        return {}
