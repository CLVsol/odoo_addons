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

class clv_family(osv.osv):
    _name = 'clv_family'

    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        reads = self.read(cr, uid, ids, ['name_code'], context=context)
        res = []
        for record in reads:
            name = record['name_code']
            res.append((record['id'], name))
        return res
    
    def name_code_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name', 'code'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['code']:
                name = name + ' [' + record['code'] + ']'
            res.append((record['id'], name))
        return res

    def _name_code_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_code_get(cr, uid, ids, context=context)
        return dict(res)

    _columns = {
        'name': fields.char('Name', required=True, size=64),
        'alias': fields.char('Alias', size=64, help='Common name that the Family is referred'),
        'code': fields.char(size=64, string='Family Code', required=False),
        'address_id': fields.many2one('res.partner', 'Family Address', ondelete='restrict'),
        'family_phone': fields.char('Family Phone', size=32),
        'mobile_phone': fields.char('Family Mobile', size=32),
        'family_email': fields.char('Family Email', size=240),
        'notes':  fields.text(string='Notes'),
        'date_inclusion': fields.datetime("Inclusion Date", required=False, readonly=False),
        'active': fields.boolean('Active', 
                                 help="If unchecked, it will allow you to hide the family without removing it."),
        'name_code': fields.function(_name_code_get_fnc, type="char", string='Name (Code)'),
        }

    _defaults = {
        'date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': 1,
        }
    
    _sql_constraints = [('family_code_uniq', 'unique(code)', u'Error! The Family Code must be unique!')]

    _order='name'

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
            return {'value': {'family_phone': address.phone, 'mobile_phone': address.mobile, 'family_email': address.email}}
        return {'value': {}}
