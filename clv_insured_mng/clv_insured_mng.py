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

class clv_insured_mng(models.Model):
    _name = 'clv_insured_mng'

    insured_id = fields.Many2one('clv_insured', 'Insured', ondelete='restrict')
    name = fields.Char('Name', required=True, size=64)
    # display_name = fields.Char('Name', compute='_compute_display_name',)
    alias = fields.Char('Alias', size=64, help='Common name that the Insured is referred')
    code = fields.Char(size=64, string='Insured Code')
    # address_id = fields.Many2one('res.partner', 'Working Address', ondelete='restrict')
    address_id = fields.Many2one('clv_address', 'Working Address', ondelete='restrict')
    # address_home_id = fields.Many2one('res.partner', 'Home Address', ondelete='restrict')
    address_home_id = fields.Many2one('clv_address', 'Home Address', ondelete='restrict')
    work_phone = fields.Char('Work Phone', size=32)
    mobile_phone = fields.Char('Work Mobile', size=32)
    work_email = fields.Char('Work Email', size=240)
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Datetime("Inclusion Date", required=False, readonly=False,
                                     default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    country_id = fields.Many2one('res.country', 'Nationality')
    birthday = fields.Date("Date of Birth")
    age = fields.Char('Age', size=32, compute='_age', store=False)
    identification_id = fields.Char('Insured ID', size=32)
    otherid = fields.Char('Other ID', size=64)
    gender = fields.Selection([('M', 'Male'),
                               ('F', 'Female')
                               ], 'Gender')
    marital = fields.Selection([('single', 'Single'), 
                                ('married', 'Married'), 
                                ('widower', 'Widower'), 
                                ('divorced', 'Divorced'),
                                ], 'Marital Status')
    batch_name = fields.Char('Batch Name', required=True, size=64)
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the insured without removing it.",
                            default=1)

    _order='name'

    _sql_constraints = [('code_uniq', 'unique(code)', u'Error! The Insured Code must be unique!')]

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

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
            return {'value': {'insured_phone': address.phone, 'mobile_phone': address.mobile, 'insured_email': address.email}}
        return {'value': {}}
