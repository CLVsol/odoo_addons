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
from openerp.osv import osv
from datetime import *
from dateutil.relativedelta import relativedelta

class clv_batch(models.Model):
    _inherit = 'clv_batch'

    size = fields.Integer(string='Size')
    item_birthday = fields.Date("Date of Birth")
    item_age = fields.Char(string='Item Age', size=32, compute='_item_age', store=False)
    batch_start = fields.Date("Batch Start",
                              default=lambda *a: datetime.now().strftime('%Y-%m-%d'))
    batch_age = fields.Char(string='Batch Age', size=32, compute='_batch_age', store=False)
    batch_end = fields.Date("Batch End")

    @api.one
    @api.depends('item_birthday')
    def _item_age(self):
        now = datetime.now()
        if self.item_birthday:
            dob = datetime.strptime(self.item_birthday,'%Y-%m-%d')
            delta=relativedelta (now, dob)
            self.item_age = str(delta.years) +"y "+ str(delta.months) +"m "+ str(delta.days)+"d"
        else:
            self.item_age = "No Item Date of Birth!"

    @api.one
    @api.depends('batch_start')
    def _batch_age(self):
        now = datetime.now()
        if self.batch_start:
            dob = datetime.strptime(self.batch_start,'%Y-%m-%d')
            delta=relativedelta (now, dob)
            self.batch_age = str(delta.years) +"y "+ str(delta.months) +"m "+ str(delta.days)+"d"
        else:
            self.batch_age = "No Item Date of Birth!"
