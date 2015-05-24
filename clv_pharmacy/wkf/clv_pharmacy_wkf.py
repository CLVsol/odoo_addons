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

class clv_pharmacy(models.Model):
    _inherit = 'clv_pharmacy'

    state_date = fields.Datetime("Status change date", required=True, readonly=True)
    state = fields.Selection([('new','New'),
                              ('active','Active'),
                              ('suspended','Suspended'),
                              ('canceled','Canceled'),
                              ], string='Status', default='new', readonly=True, required=True, help="")

    _defaults = {
        'state_date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
    
    @api.one
    def button_new(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'new'

    @api.one
    def button_activate(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'active'

    @api.one
    def button_suspend(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'suspended'

    @api.one
    def button_cancel(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'canceled'
