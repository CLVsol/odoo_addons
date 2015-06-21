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
from datetime import datetime
from dateutil.relativedelta import relativedelta

class clv_insured(models.Model):
    _inherit = 'clv_insured'

    state_date = fields.Datetime("Status change date", required=True, readonly=True,
                                 default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # state_age = fields.Char('Status Age', size=32, compute='_state_age', store=False)
    date_activation = fields.Date("Activation date", required=False, readonly=False)
    date_cancelation = fields.Date("Cancelation date", required=False, readonly=False)
    state = fields.Selection([('new','New'),
                              ('processing','Processing'),
                              ('active','Active'),
                              ('suspended','Suspended'),
                              ('canceled','Canceled')
                              ], string='Status', default='new', readonly=True, required=True, help="")

    # @api.one
    # @api.depends('state_date')
    # def _state_age(self):
    #     now = datetime.now()
    #     if self.state_date:
    #         dob = datetime.strptime(self.state_date,'%Y-%m-%d %H:%M:%S')
    #         delta=relativedelta (now, dob)
    #         self.state_age = str(delta.years) +"y "+ str(delta.months) +"m "+ str(delta.days)+"d"
    #     else:
    #         self.state_age = "No Status change date!"

    @api.one
    def button_new(self):
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'new'

    @api.one
    def button_process(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'processing'

    @api.one
    def button_activate(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if not self.date_activation:
            self.date_activation = datetime.now().strftime('%Y-%m-%d')
            time.sleep(1.0)
        self.state = 'active'

    @api.one
    def button_suspend(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = 'suspended'

    @api.one
    def button_cancel(self):
        self.state_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if not self.date_cancelation:
            self.date_cancelation = datetime.now().strftime('%Y-%m-%d')
            time.sleep(1.0)
        self.state = 'canceled'
