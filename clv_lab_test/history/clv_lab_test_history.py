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


class clv_lab_test_history(models.Model):
    _name = 'clv_lab_test.history'

    lab_test_id = fields.Many2one('clv_lab_test', 'Patient', required=True)
    user_id = fields.Many2one('res.users', 'User', required=True,
                              default=lambda self: self._uid)
    date = fields.Datetime("Date", required=True,
                           default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    state = fields.Selection([('draft', 'Draft'),
                              ('collected', 'Collected'),
                              ('testing', 'Testing'),
                              ('done', 'Done'),
                              ('approved', 'Approved'),
                              ('canceled', 'Canceled'),
                              ], string='Status', default='draft', readonly=True, required=True, help="")
    notes = fields.Text(string='Notes')

    _order = "date desc"


class clv_lab_test(models.Model):
    _inherit = 'clv_lab_test'

    history_ids = fields.One2many('clv_lab_test.history', 'lab_test_id', 'Lab Test History', readonly=True)
    active_history = fields.Boolean('Active History',
                                    help="If unchecked, it will allow you to disable the history without removing it.",
                                    default=False)

    @api.one
    def insert_clv_lab_test_history(self, lab_test_id, state, notes):
        if self.active_history:
            values = {
                'lab_test_id':  lab_test_id,
                'state': state,
                'notes': notes,
            }
            self.pool.get('clv_lab_test.history').create(self._cr, self._uid, values)

    @api.multi
    def write(self, values):
        if ('state' not in values) and ('date' not in values):
            notes = values.keys()
            self.insert_clv_lab_test_history(self.id, self.state, notes)
        return super(clv_lab_test, self).write(values)

    @api.one
    def button_draft(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'draft'
        self.insert_clv_lab_test_history(self.id, 'draft', '')

    @api.one
    def button_collected(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'collected'
        self.insert_clv_lab_test_history(self.id, 'collected', '')

    @api.one
    def button_testing(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'testing'
        self.insert_clv_lab_test_history(self.id, 'testing', '')

    @api.one
    def button_done(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'done'
        self.insert_clv_lab_test_history(self.id, 'done', '')

    @api.one
    def button_approve(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'approved'
        self.insert_clv_lab_test_history(self.id, 'approved', '')

    @api.one
    def button_cancel(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'canceled'
        self.insert_clv_lab_test_history(self.id, 'canceled', '')
