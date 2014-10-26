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

class clv_tag_history(osv.osv):
    _name = 'clv_tag.history'

    _columns = {
        'tag_id': fields.many2one('clv_tag', 'Tag', required=True, ondelete='cascade'),
        'user_id':fields.many2one ('res.users', 'User', required=True),
        'date': fields.datetime("Date", required=True),
        'state': fields.selection([('draft','Draft'),
                                   ('revised','Revised'),
                                   ('done','Done')
                                   ], string='Status', readonly=True, required=True, help=""),
        'notes': fields.text(string='Notes'),
        }
    
    _defaults = {
        'user_id': lambda self: self._uid,
        'date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'state': 'draft',
        }

    _order = "date desc"

class clv_tag(osv.osv):
    _inherit = 'clv_tag'

    _columns = {
        'history_ids': fields.one2many('clv_tag.history', 'tag_id', 'Tag History', readonly=True),
        'active_history': fields.boolean('Active History', 
                                         help="If unchecked, it will allow you to disable the history without removing it."),
        }
    
    _defaults = {
        'active_history': True
        }


    def insert_clv_tag_history(self, cr, uid, active_history, tag_id, state, notes, context=None):
        if context is None:
            context = {}
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if active_history:
            vals = { 
                'tag_id': tag_id,
                'user_id': uid,
                'date': date,
                'state': state,
                'notes': notes,
            }
            self.pool.get('clv_tag.history').create(cr, uid, vals, context)

    def write(self, cr, uid, ids, vals, context=None):
        if context is None:
            context = {}
        if (not 'state' in vals) and (not 'date' in vals) and (not 'history_ids' in vals):
            notes = vals.keys()
            for tag in self.browse(cr, uid, ids):
                if 'active_history' in vals:
                    self.insert_clv_tag_history(cr, uid, True, tag.id, tag.state, notes)
                else:
                    self.insert_clv_tag_history(cr, uid, tag.active_history, tag.id, tag.state, notes)
        return super(clv_tag, self).write(cr, uid, ids, vals, context)

    def button_draft(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'draft'})
        for tag in self.browse(cr, uid, ids):
            self.insert_clv_tag_history(cr, uid, tag.active_history, tag.id, 'draft', '')

    def button_revised(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'revised'})
        for tag in self.browse(cr, uid, ids):
            self.insert_clv_tag_history(cr, uid, tag.active_history, tag.id, 'revised', '')

    def button_done(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'done'})
        for tag in self.browse(cr, uid, ids):
            self.insert_clv_tag_history(cr, uid, tag.active_history, tag.id, 'done', '')
