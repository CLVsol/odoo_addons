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

class clv_seedling(models.Model):
    _name = 'clv_seedling'

    name = fields.Char('Name', required=True, size=64)
    alias = fields.Char('Alias', size=64, help='Common name that the Seedling is referred')
    code = fields.Char(size=64, string='Seedling Code')
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Datetime("Inclusion Date", required=False, readonly=False,
                                     default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    birthday = fields.Date("Date of Birth")
    age = fields.Char('Age', size=32, compute='_age', store=False)
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the seedling without removing it.",
                            default=1)

    _order='name'

    _sql_constraints = [('code_uniq', 'unique(code)', u'Error! The Seedling Code must be unique!')]

    @api.onchange('name')
    def _onchange_name(self):
        if not self.alias:
            self.alias = self.name

    @api.one
    @api.depends('birthday')
    def _age(self):
        now = datetime.now()
        if self.birthday:
            dob = datetime.strptime(self.birthday,'%Y-%m-%d')
            delta=relativedelta (now, dob)
            self.age = str(delta.years) +"y "+ str(delta.months) +"m "+ str(delta.days)+"d"
        else:
            self.age = "No Date of Birth!"
