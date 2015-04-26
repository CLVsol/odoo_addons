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


class clv_medicament_active_component(osv.osv):
    _name = 'clv_medicament.active_component'

    _columns = {
        'name': fields.char(size=256, string='Active Component', required=True),
        'code': fields.char(size=256, string='Code'),
        'info': fields.text(string='Info'),
        'active': fields.boolean('Active', 
                                 help="The active field allows you to hide the therapeutic class without removing it."),
        'medicament_ids': fields.one2many('clv_medicament', 'active_component', 'Medicaments'),

        }
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Active Component must be unique!'),
        ('code_uniq', 'UNIQUE(code)', 'Code must be unique!'),
        ]   

    _order='name'

    _defaults = {
        'active': 1,
        }

class clv_medicament(osv.osv):
    _inherit = 'clv_medicament'

    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        reads = self.read(cr, uid, ids, ['name_active_component'], context=context)
        res = []
        for record in reads:
            name = record['name_active_component']
            res.append((record['id'], name))
        return res
    
    def name_active_component_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name', 'active_component_name'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['active_component_name']:
                name = name + ' (' + record['active_component_name'] + ')'
            res.append((record['id'], name))
        return res

    def _name_active_component_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_active_component_get(cr, uid, ids, context=context)
        return dict(res)

    _columns = {
        'active_component': fields.many2one('clv_medicament.active_component', 
                                            string='Active Component', 
                                            help='Medicament Active Component'),
        'name_active_component': fields.function(_name_active_component_get_fnc, type="char", 
                                                 string='Name (Active Component)'),
        'active_component_name': fields.related('active_component', 'name', type='char', 
                                                string='Related Active Component', 
                                                readonly=True, store=True),
        }
