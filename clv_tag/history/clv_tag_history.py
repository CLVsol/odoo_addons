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

#from openerp import models, fields, api, netsvc
from openerp.osv import fields, osv
from datetime import *

#class clv_tag_history(models.Model):
class clv_tag_history(osv.osv):
    _name = 'clv_tag.history'

    # tag_id = fields.Many2one('clv_tag', 'Tag', required=True)
    # user_id = fields.Many2one ('res.users', 'User', required=True,
    #                            default=lambda self: self._uid)
    # date = fields.Datetime("Date", required=True,
    #                        default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # state = fields.Selection([('draft','Draft'),
    #                           ('revised','Revised'),
    #                           ('done','Done')
    #                           ], string='Status', default='draft', readonly=True, required=True, help="")
    # notes = fields.Text(string='Notes')
    
    _columns = {
        'tag_id': fields.many2one('clv_tag', 'Tag', required=True),
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

#class clv_tag(models.Model):
class clv_tag(osv.osv):
    _inherit = 'clv_tag'

    # history_ids = fields.One2many('clv_tag.history', 'tag_id', 'Tag History', readonly=True)
    # active_history = fields.Boolean('Active History', 
    #                                 help="If unchecked, it will allow you to disable the history without removing it.",
    #                                 default=False)
    _columns = {
        'history_ids': fields.one2many('clv_tag.history', 'tag_id', 'Tag History', readonly=True),
        'active_history': fields.boolean('Active History', 
                                         help="If unchecked, it will allow you to disable the history without removing it."),
        }
    
    _defaults = {
        'active_history': False
        }


    #@api.one
    #def insert_clv_tag_history(self, tag_id, state, notes):
    def insert_clv_tag_history(self, cr, uid, active_history, tag_id, state, notes, context=None):
        # if self.active_history:
        #     vals = { 
        #         'tag_id': tag_id,
        #         'state': state,
        #         'notes': notes,
        #     }
        #     self.pool.get('clv_tag.history').create(self._cr, self._uid, vals)
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

    #@api.multi
    #def write(self, vals):
    def write(self, cr, uid, ids, vals, context=None):
        if context is None:
            context = {}
        if (not 'state' in vals) and (not 'date' in vals):
            notes = vals.keys()
            #self.insert_clv_tag_history(self.id, self.state, notes)
            for tag in self.browse(cr, uid, ids):
                self.insert_clv_tag_history(cr, uid, tag.active_history, tag.id, 'revised', notes)
        #return super(clv_tag, self).write(vals)
        return super(clv_tag, self).write(cr, uid, ids, vals, context)

    #@api.one
    #def button_draft(self):
    def button_draft(self, cr, uid, ids):
        #self.state = 'draft'
        self.write(cr, uid, ids, {'state': 'draft'})
        #self.insert_clv_tag_history(self.id, 'draft', '')
        for tag in self.browse(cr, uid, ids):
            self.insert_clv_tag_history(cr, uid, tag.active_history, tag.id, 'draft', '')

    #@api.one
    #def button_revised(self):
    def button_revised(self, cr, uid, ids):
        #self.state = 'revised'
        self.write(cr, uid, ids, {'state': 'revised'})
        #self.insert_clv_tag_history(self.id, 'revised', '')
        for tag in self.browse(cr, uid, ids):
            self.insert_clv_tag_history(cr, uid, tag.active_history, tag.id, 'revised', '')

    #@api.one
    #def button_done(self):
    def button_done(self, cr, uid, ids):
        #self.state = 'done'
        self.write(cr, uid, ids, {'state': 'done'})
        #self.insert_clv_tag_history(self.id, 'done', '')
        for tag in self.browse(cr, uid, ids):
            self.insert_clv_tag_history(cr, uid, tag.active_history, tag.id, 'done', '')
