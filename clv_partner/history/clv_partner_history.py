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
from datetime import *

class res_partner_history(osv.osv):
    _name = 'res.partner.history'

    _order = "date desc"

    _columns = {
        'partner_id': fields.many2one('res.partner', 'partner', required=True, ondelete='cascade'),
        'user_id':fields.many2one ('res.users', 'User', required=True),
        'date': fields.datetime("Date", required=True),
        'notes': fields.text(string='Notes'),
        }
    
    _defaults = {
        'user_id': lambda self: self._uid,
        'date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }

    _order = "date desc"

class res_partner(osv.osv):
    _inherit = 'res.partner'

    _columns = {
        'history_ids': fields.one2many('res.partner.history', 'partner_id', 'partner History', readonly=True),
        'active_history': fields.boolean('active History', 
                                         help="If unchecked, it will allow you to disable the history without removing it."),
        }
    
    _defaults = {
        'active_history': True
        }

    def insert_res_partner_history(self, cr, uid, active_history, partner_id, notes, context=None):
        if context is None:
            context = {}
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if active_history:
            vals = { 
                'partner_id': partner_id,
                'user_id': uid,
                'date': date,
                'notes': notes,
            }
            self.pool.get('res.partner.history').create(cr, uid, vals, context)

    def create(self, cr, uid, vals, context=None):
        if context is None:
            context = {}
        notes = 'partner creation'
        create_super = super(res_partner, self).create(cr, uid, vals, context)
        if 'active_history' in vals:
            self.insert_res_partner_history(cr, uid, vals['active_history'], create_super, notes)
        else:
            self.insert_res_partner_history(cr, uid, False, create_super, notes)
        return create_super

    def write(self, cr, uid, ids, vals, context=None):
        if context is None:
            context = {}
        if (not 'history_ids' in vals):
            notes = vals.keys()
            for partner in self.browse(cr, uid, ids):
                if 'active_history' in vals:
                    self.insert_res_partner_history(cr, uid, True, partner.id, notes)
                else:
                    self.insert_res_partner_history(cr, uid, partner.active_history, partner.id, notes)
        return super(res_partner, self).write(cr, uid, ids, vals, context)
