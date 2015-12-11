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


class clv_person_mng(models.Model):
    _name = 'clv_person_mng'

    person_id = fields.Many2one('clv_person', 'Person', ondelete='restrict')
    name = fields.Char('Name', required=True, size=64)
    alias = fields.Char('Alias', size=64, help='Common name that the Person is referred')
    code = fields.Char(size=64, string='Person Code')
    address_id = fields.Many2one('clv_address', 'Person Address', ondelete='restrict')
    person_phone = fields.Char('Person Phone', size=32)
    mobile_phone = fields.Char('Person Mobile', size=32)
    person_email = fields.Char('Person Email', size=240)
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Datetime("Inclusion Date", required=False, readonly=False,
                                     default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    country_id = fields.Many2one('res.country', 'Nationality')
    birthday = fields.Date("Date of Birth")
    age = fields.Char('Age', size=32, compute='_age', store=False)
    spouse = fields.Char('Spouse', required=False, size=64)
    spouse_id = fields.Many2one('clv_person', 'Spouse', ondelete='restrict')
    father = fields.Char('Father', required=False, size=64)
    father_id = fields.Many2one('clv_person', 'Father', ondelete='restrict')
    mother = fields.Char('Mother', required=False, size=64)
    mother_id = fields.Many2one('clv_person', 'Mother', ondelete='restrict')
    responsible = fields.Char('Responsible', required=False, size=64)
    responsible_id = fields.Many2one('clv_person', 'Responsible', ondelete='restrict')
    identification_id = fields.Char('Person ID', size=32)
    otherid = fields.Char('Other ID', size=64)
    gender = fields.Selection([('M', 'Male'),
                               ('F', 'Female')
                               ], 'Gender')
    marital = fields.Selection([('single', 'Single'),
                                ('married', 'Married'),
                                ('widower', 'Widower'),
                                ('divorced', 'Divorced'),
                                ], 'Marital Status')
    batch_name = fields.Char('Batch Name', required=False, size=64)
    active = fields.Boolean('Active',
                            help="If unchecked, it will allow you to hide the person without removing it.",
                            default=1)

    _order = 'name'

    _sql_constraints = [('code_uniq', 'unique(code)', u'Error! The Person Code must be unique!')]

    @api.onchange('name')
    def _onchange_name(self):
        if not self.alias:
            self.alias = self.name

    @api.one
    @api.depends('birthday')
    def _age(self):
        now = datetime.now()
        if self.birthday:
            dob = datetime.strptime(self.birthday, '%Y-%m-%d')
            delta = relativedelta(now, dob)
            self.age = str(delta.years) + "y " + str(delta.months) + "m " + str(delta.days) + "d"
        else:
            self.age = "No Date of Birth!"

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
            return {'value': {'person_phone': address.phone,
                              'mobile_phone': address.mobile,
                              'person_email': address.email
                              }}
        return {'value': {}}
