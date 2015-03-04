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

class clv_insurance_client_history(models.Model):
    _name = 'clv_insurance_client.history'

    insurance_client_id = fields.Many2one('clv_insurance_client', 'Insurance Client', required=True)
    user_id = fields.Many2one ('res.users', 'User', required=True)
    date = fields.Datetime("Date", required=True)
    state = fields.Selection([('new','New'),
                              ('active','Active'),
                              ('suspended','Suspended'),
                              ('canceled','Canceled'),
                              ], string='Status', default='new', readonly=True, required=True, help="")
    notes = fields.Text(string='Notes')
    
    _order = "date desc"

    _defaults = {
        'user_id': lambda obj,cr,uid,context: uid, 
        'date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }

class clv_insurance_client(models.Model):
    _inherit = 'clv_insurance_client'

    history_ids = fields.One2many('clv_insurance_client.history', 'insurance_client_id', 'Insurance Client History', readonly=True)
    active_history = fields.Boolean('Active History', 
                                    help="If unchecked, it will allow you to disable the history without removing it.",
                                    default=True)

    @api.one
    def insert_clv_insurance_client_history(self, insurance_client_id, state, notes):
        if self.active_history:
            values = { 
                'insurance_client_id':  insurance_client_id,
                'state': state,
                'notes': notes,
            }
            self.pool.get('clv_insurance_client.history').create(self._cr, self._uid, values)

    @api.multi
    def write(self, values):
        if (not 'state' in values) and (not 'date' in values):
            #date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            #values['date'] = date
            notes = values.keys()
            self.insert_clv_insurance_client_history(self.id, self.state, notes)
        return super(clv_insurance_client, self).write(values)

    @api.one
    def button_new(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'new'
        self.insert_clv_insurance_client_history(self.id, 'new', '')

    @api.one
    def button_activate(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'active'
        self.insert_clv_insurance_client_history(self.id, 'active', '')

    @api.one
    def button_suspend(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'suspended'
        self.insert_clv_insurance_client_history(self.id, 'suspended', '')

    @api.one
    def button_cancel(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'canceled'
        self.insert_clv_insurance_client_history(self.id, 'canceled', '')
