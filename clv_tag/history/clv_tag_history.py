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

from openerp import models, fields, api, netsvc
from datetime import *

class clv_tag_history(models.Model):
    _name = 'clv_tag.history'

    tag_id = fields.Many2one('clv_tag', 'Tag', required=True)
    user_id = fields.Many2one ('res.users', 'User', required=True,
                               default=lambda self: self._uid)
    date = fields.Datetime("Date", required=True,
                           default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    state = fields.Selection([('draft','Draft'),
                              ('revised','Revised'),
                              ('done','Done')
                              ], string='Status', default='draft', readonly=True, required=True, help="")
    notes = fields.Text(string='Notes')
    
    _order = "date desc"

class clv_tag(models.Model):
    _inherit = 'clv_tag'

    history_ids = fields.One2many('clv_tag.history', 'tag_id', 'Tag History', readonly=True)

    @api.one
    def insert_clv_tag_history(self, tag_id, state, notes):
        vals = { 
            'tag_id': tag_id,
            'state': state,
            'notes': notes,
        }
        self.pool.get('clv_tag.history').create(self._cr, self._uid, vals)

    @api.multi
    def write(self, vals):
        if (not 'state' in vals) and (not 'date' in vals):
            notes = vals.keys()
            self.insert_clv_tag_history(self.id, self.state, notes)
        return super(clv_tag, self).write(vals)

    @api.one
    def button_draft(self):
        self.state = 'draft'
        self.insert_clv_tag_history(self.id, 'draft', '')

    @api.one
    def button_revised(self):
        self.state = 'revised'
        self.insert_clv_tag_history(self.id, 'revised', '')

    @api.one
    def button_done(self):
        self.state = 'done'
        self.insert_clv_tag_history(self.id, 'done', '')
