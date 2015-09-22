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

class clv_medicament_dispensation_ext_history(osv.osv):
    _name = 'clv_medicament_dispensation_ext.history'

    _order = "date desc"

    _columns = {
        'medicament_dispensation_ext_id': fields.many2one('clv_medicament_dispensation_ext', 'medicament_dispensation_ext', 
                                                      required=True, ondelete='cascade'),
        'user_id':fields.many2one ('res.users', 'User', required=True),
        'date': fields.datetime("Date", required=True),
        'state': fields.selection([('draft','Draft'),
                                   ('waiting','Waiting'),
                                   ('pre_authorized','Pre Authorized'),
                                   ('authorized','Authorized'),
                                   ('not_authorized','Not Authorized'),
                                   ('canceled','Canceled'),
                                   ('proceeding','Proceeding'),
                                   ('reconciled','Reconciled'),
                                   ('not_reconciled','Not Reconciled'),
                                   ], string='Status', readonly=True, required=True, help=""),
        'notes': fields.text(string='Notes'),
        }
    
    _defaults = {
        'user_id': lambda self: self._uid,
        'date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'state': 'draft',
        }

    _order = "date desc"

class clv_medicament_dispensation_ext(osv.osv):
    _inherit = 'clv_medicament_dispensation_ext'

    _columns = {
        'history_ids': fields.one2many('clv_medicament_dispensation_ext.history', 'medicament_dispensation_ext_id', 'Medicament History', readonly=True),
        'active_history': fields.boolean('Active History', 
                                         help="If unchecked, it will allow you to disable the history without removing it."),
        }
    
    _defaults = {
        'active_history': True
        }

    def insert_clv_medicament_dispensation_ext_history(self, cr, uid, active_history, medicament_dispensation_ext_id, state, notes, context=None):
        if context is None:
            context = {}
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if active_history:
            vals = { 
                'medicament_dispensation_ext_id': medicament_dispensation_ext_id,
                'user_id': uid,
                'date': date,
                'state': state,
                'notes': notes,
            }
            self.pool.get('clv_medicament_dispensation_ext.history').create(cr, uid, vals, context)

    def write(self, cr, uid, ids, vals, context=None):
        if context is None:
            context = {}
        if (not 'state' in vals) and (not 'date' in vals) and (not 'history_ids' in vals):
            notes = vals.keys()
            try:
                for medicament_dispensation_ext in self.browse(cr, uid, ids):
                    if 'active_history' in vals:
                        self.insert_clv_medicament_dispensation_ext_history(cr, uid, True, medicament_dispensation_ext.id, medicament_dispensation_ext.state, notes)
                    else:
                        self.insert_clv_medicament_dispensation_ext_history(cr, uid, medicament_dispensation_ext.active_history, medicament_dispensation_ext.id, medicament_dispensation_ext.state, notes)
            except:
                pass
        return super(clv_medicament_dispensation_ext, self).write(cr, uid, ids, vals, context)

    def button_draft(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                  'state': 'draft'})
        for medicament_dispensation_ext in self.browse(cr, uid, ids):
            self.insert_clv_medicament_dispensation_ext_history(cr, uid, medicament_dispensation_ext.active_history, medicament_dispensation_ext.id, 'draft', '')

    def button_waiting(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  'state': 'waiting'})
        for medicament_dispensation_ext in self.browse(cr, uid, ids):
            self.insert_clv_medicament_dispensation_ext_history(cr, uid, medicament_dispensation_ext.active_history, medicament_dispensation_ext.id, 'waiting', '')

    def button_pre_authorize(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  'state': 'pre_authorized'})
        for medicament_dispensation_ext in self.browse(cr, uid, ids):
            self.insert_clv_medicament_dispensation_ext_history(cr, uid, medicament_dispensation_ext.active_history, medicament_dispensation_ext.id, 'pre_authorized', '')

    def button_authorize(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  'state': 'authorized'})
        for medicament_dispensation_ext in self.browse(cr, uid, ids):
            self.insert_clv_medicament_dispensation_ext_history(cr, uid, medicament_dispensation_ext.active_history, medicament_dispensation_ext.id, 'authorized', '')

    def button_do_not_authorize(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                  'state': 'not_authorized'})
        for medicament_dispensation_ext in self.browse(cr, uid, ids):
            self.insert_clv_medicament_dispensation_ext_history(cr, uid, medicament_dispensation_ext.active_history, medicament_dispensation_ext.id, 'not_authorized', '')

    def button_cancel(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                  'state': 'canceled'})
        for medicament_dispensation_ext in self.browse(cr, uid, ids):
            self.insert_clv_medicament_dispensation_ext_history(cr, uid, medicament_dispensation_ext.active_history, medicament_dispensation_ext.id, 'canceled', '')

    def button_proceeding(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  'state': 'proceeding'})
        for medicament_dispensation_ext in self.browse(cr, uid, ids):
            self.insert_clv_medicament_dispensation_ext_history(cr, uid, medicament_dispensation_ext.active_history, medicament_dispensation_ext.id, 'not_authorized', '')

    def button_reconcile(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  'state': 'reconciled'})
        for medicament_dispensation_ext in self.browse(cr, uid, ids):
            self.insert_clv_medicament_dispensation_ext_history(cr, uid, medicament_dispensation_ext.active_history, medicament_dispensation_ext.id, 'not_authorized', '')

    def button_do_not_reconcile(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                  'state': 'not_reconciled'})
        for medicament_dispensation_ext in self.browse(cr, uid, ids):
            self.insert_clv_medicament_dispensation_ext_history(cr, uid, medicament_dispensation_ext.active_history, medicament_dispensation_ext.id, 'not_authorized', '')
