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
#import time

class clv_person_history(osv.osv):
    _name = 'clv_person.history'

    _order = "date desc"

    _columns = {
        'person_id': fields.many2one('clv_person', 'person', required=True, ondelete='cascade'),
        'user_id':fields.many2one ('res.users', 'User', required=True),
        'date': fields.datetime("Date", required=True),
        'state': fields.selection([('new','New'),
                                   ('active','active'),
                                   ('inactive','Inactive'),
                                   ('suspended','Suspended'),
                                   ], string='Status', readonly=True, required=True, help=""),
        'notes': fields.text(string='Notes'),
        }
    
    _defaults = {
        'user_id': lambda self: self._uid,
        'date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'state': 'new',
        }

    _order = "date desc"

class clv_person(osv.osv):
    _inherit = 'clv_person'

    _columns = {
        'history_ids': fields.one2many('clv_person.history', 'person_id', 'person History', readonly=True),
        'active_history': fields.boolean('active History', 
                                         help="If unchecked, it will allow you to disable the history without removing it."),
        }
    
    _defaults = {
        'active_history': True
        }

    def insert_clv_person_history(self, cr, uid, active_history, person_id, state, notes, context=None):
        if context is None:
            context = {}
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if active_history:
            vals = { 
                'person_id': person_id,
                'user_id': uid,
                'date': date,
                'state': state,
                'notes': notes,
            }
            self.pool.get('clv_person.history').create(cr, uid, vals, context)

    def write(self, cr, uid, ids, vals, context=None):
        if context is None:
            context = {}
        if (not 'state' in vals) and (not 'date' in vals) and (not 'history_ids' in vals):
            notes = vals.keys()
            for person in self.browse(cr, uid, ids):
                if 'active_history' in vals:
                    self.insert_clv_person_history(cr, uid, True, person.id, person.state, notes)
                else:
                    self.insert_clv_person_history(cr, uid, person.active_history, person.id, person.state, notes)
        return super(clv_person, self).write(cr, uid, ids, vals, context)

    def button_new(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                  'state': 'new'})
        for person in self.browse(cr, uid, ids):
            self.insert_clv_person_history(cr, uid, person.active_history, person.id, 'new', '')

    def button_activate(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  'date_activation':  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  'state': 'active'})
        for person in self.browse(cr, uid, ids):
            self.insert_clv_person_history(cr, uid, person.active_history, person.id, 'active', '')

    def button_inactivate(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                  'date_inactivation':  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  'state': 'inactive'})
        for person in self.browse(cr, uid, ids):
            self.insert_clv_person_history(cr, uid, person.active_history, person.id, 'inactive', '')

    def button_suspend(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                  'date_suspension':  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  'state': 'suspended'})
        for person in self.browse(cr, uid, ids):
            self.insert_clv_person_history(cr, uid, person.active_history, person.id, 'suspended', '')
