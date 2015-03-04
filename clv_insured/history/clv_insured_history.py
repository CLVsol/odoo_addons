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
import time

class clv_insured_history(models.Model):
    _name = 'clv_insured.history'

    insured_id = fields.Many2one('clv_insured', 'Insured', required=True)
    user_id = fields.Many2one ('res.users', 'User', required=True,
                               default=lambda self: self._uid)
    date = fields.Datetime("Date", required=True,
                           default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    state = fields.Selection([('new','New'),
                              ('active','Active'),
                              ('suspended','Suspended'),
                              ('canceled','Canceled')
                              ], string='Status', default='new', readonly=True, required=True, help="")
    notes = fields.Text(string='Notes')
    
    _order = "date desc"

class clv_insured(models.Model):
    _inherit = 'clv_insured'

    history_ids = fields.One2many('clv_insured.history', 'insured_id', 'Insured History', readonly=True)
    active_history = fields.Boolean('Active History', 
                                    help="If unchecked, it will allow you to disable the history without removing it.",
                                    default=True)

    @api.one
    def insert_clv_insured_history(self, insured_id, state, notes):
        if self.active_history:
            values = { 
                'insured_id':  insured_id,
                'state': state,
                'notes': notes,
            }
            self.pool.get('clv_insured.history').create(self._cr, self._uid, values)

    @api.multi
    def write(self, values):
        if (not 'state' in values) and (not 'state_date' in values):
            notes = values.keys()
            self.insert_clv_insured_history(self.id, self.state, notes)
        return super(clv_insured, self).write(values)

    @api.one
    def button_new(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'new'
        self.insert_clv_insured_history(self.id, 'new', '')

    @api.one
    def button_activate(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # if not self.date_activation:
        #     self.date_activation = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #     time.sleep(1.0)
        self.state = 'active'
        self.insert_clv_insured_history(self.id, 'active', '')

    @api.one
    def button_suspend(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # if not self.date_suspension:
        #     self.date_suspension = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #     time.sleep(1.0)
        self.state = 'suspended'
        self.insert_clv_insured_history(self.id, 'suspended', '')

    @api.one
    def button_cancel(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # if not self.date_inactivation:
        #     self.date_inactivation = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #     time.sleep(1.0)
        self.state = 'canceled'
        self.insert_clv_insured_history(self.id, 'canceled', '')
