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
from datetime import *

class clv_annotation_history(models.Model):
    _name = 'clv_annotation.history'

    annotation_id = fields.Many2one('clv_annotation', 'Annotation', required=True)
    user_id = fields.Many2one ('res.users', 'User', required=True)
    date = fields.Datetime("Date", required=True)
    state = fields.Selection([('draft','Draft'),
                              ('revised','Revised'),
                              ('waiting','Waiting'),
                              ('done','Done')
                              ], string='Status', default='draft', readonly=True, required=True, help="")
    notes = fields.Text(string='Notes')
    
    _order = "date desc"

    _defaults = {
        'user_id': lambda obj,cr,uid,context: uid, 
        'date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }

class clv_annotation(models.Model):
    _inherit = 'clv_annotation'

    history_ids = fields.One2many('clv_annotation.history', 'annotation_id', 'Annotation History', readonly=True)
    active_history = fields.Boolean('Active History', 
                                    help="If unchecked, it will allow you to disable the history without removing it.",
                                    default=True)

    @api.one
    def insert_clv_annotation_history(self, annotation_id, state, notes):
        if self.active_history:
            values = { 
                'annotation_id':  annotation_id,
                'state': state,
                'notes': notes,
            }
            self.pool.get('clv_annotation.history').create(self._cr, self._uid, values)

    @api.multi
    def write(self, values):
        if (not 'state' in values) and (not 'date' in values):
            notes = values.keys()
            self.insert_clv_annotation_history(self.id, self.state, notes)
        return super(clv_annotation, self).write(values)

    @api.one
    def button_draft(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'draft'
        self.insert_clv_annotation_history(self.id, 'draft', '')

    @api.one
    def button_revised(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'revised'
        self.insert_clv_annotation_history(self.id, 'revised', '')

    @api.one
    def button_waiting(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'waiting'
        self.insert_clv_annotation_history(self.id, 'waiting', '')

    @api.one
    def button_done(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'done'
        self.insert_clv_annotation_history(self.id, 'done', '')
