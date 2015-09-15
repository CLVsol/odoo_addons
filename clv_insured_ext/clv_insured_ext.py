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

class clv_insured_ext(models.Model):
    _name = 'clv_insured_ext'

    name = fields.Char('Name', required=True, size=64)
    code = fields.Char(size=64, string='Insured (Ext) Code')
    address_id = fields.Many2one('clv_address', 'Address', ondelete='restrict')
    phone = fields.Char('Work Phone', size=32)
    mobile = fields.Char('Work Mobile', size=32)
    email = fields.Char('Work Email', size=240)
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Datetime("Inclusion Date", required=False, readonly=False,
                                     default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    birthday = fields.Date("Date of Birth")
    age = fields.Char('Age', size=32, compute='_age', store=False)
    identification_id = fields.Char('Insured ID', size=32)
    otherid = fields.Char('Other ID', size=64)
    gender = fields.Selection([('M', 'Male'),
                               ('F', 'Female')
                               ], 'Gender')
    synchronized = fields.Boolean('Synchronized', 
                                  help="If not checked, the Insured Information needs sincronization.",
                                  default=False)
    processing_synchronization = fields.Boolean('Processing Synchronization', 
                                                help="If checked, the synchronization is in process.",
                                                default=False)
    date_synchronization = fields.Datetime("Synchronization Date", required=False, readonly=False)
    date_previous_synchronization = fields.Datetime("Previous Synchronization Date", 
                                                    required=False, readonly=False)
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the insured_ext without removing it.",
                            default=1)

    _order='name'

    # _sql_constraints = [('code_uniq', 'unique(code)', u'Error! The Insured (Ext) Code must be unique!')]

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
            address = self.pool.get('clv_address').browse(cr, uid, address, context=context)
            return {'value': {'phone': address.phone, 'mobile': address.mobile, 'email': address.email}}
        return {'value': {}}
