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

class clv_seedling(models.Model):
    _inherit = 'clv_seedling'

    date = fields.Datetime("Status change date", required=True, readonly=True,
                           default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    date_activation = fields.Datetime("Activation date", required=False, readonly=False)
    date_inactivation = fields.Datetime("Inactivation date", required=False, readonly=False)
    date_suspension = fields.Datetime("Suspension date", required=False, readonly=False)
    state = fields.Selection([('new','New'),
                              ('active','Active'),
                              ('inactive','Inactive'),
                              ('suspended','Suspended')
                              ], string='Status', default='new', readonly=True, required=True, help="")

   
    @api.one
    def button_new(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'new'

    @api.one
    def button_activate(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if not self.date_activation:
            self.date_activation = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            time.sleep(1.0)
        self.state = 'active'

    @api.one
    def button_inactivate(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if not self.date_inactivation:
            self.date_inactivation = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            time.sleep(1.0)
        self.state = 'inactive'

    @api.one
    def button_suspend(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if not self.date_suspension:
            self.date_suspension = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            time.sleep(1.0)
        self.state = 'suspended'
