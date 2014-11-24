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

from openerp.osv import fields, osv
from datetime import datetime
from dateutil.relativedelta import relativedelta

class clv_person_mng(osv.osv):
    _name = 'clv_person_mng'

    def _age(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        now = datetime.now()
        for r in self.browse(cr, uid, ids, context=context):
            if r.birthday:
                dob = datetime.strptime(r.birthday,'%Y-%m-%d')
                delta=relativedelta (now, dob)
                result[r.id] = str(delta.years) +"y "+ str(delta.months) +"m "+ str(delta.days)+"d"
            else:
                result[r.id] = "No Date of Birth!"
        return result

    _columns = {
        'name': fields.char('Name', required=True, size=64),
        'alias': fields.char('Alias', size=64, help='Common name that the Person is referred'),
        'code': fields.char(size=64, string='Person Code', required=False),
        'address_id': fields.many2one('res.partner', 'Person Address', ondelete='restrict'),
        'person_phone': fields.char('Person Phone', size=32),
        'mobile_phone': fields.char('Person Mobile', size=32),
        'person_email': fields.char('Person Email', size=240),
        'notes':  fields.text(string='Notes'),
        'date_inclusion': fields.datetime("Inclusion Date", required=False, readonly=False),
        'country_id':  fields.many2one('res.country', 'Nationality'),
        'birthday':  fields.date("Date of Birth"),
        'age': fields.function(_age, type="char", string='Age', store=False),
        'spouse_id':  fields.many2one('clv_person_mng', 'Spouse', ondelete='restrict'),
        'father_id': fields.many2one('clv_person_mng', 'Father', ondelete='restrict'),
        'mother_id': fields.many2one('clv_person_mng', 'Mother', ondelete='restrict'),
        'responsible_id': fields.many2one('clv_person_mng', 'Responsible', ondelete='restrict'),
        'identification_id': fields.char('Person ID', size=32),
        'otherid': fields.char('Other ID', size=64),
        'gender':  fields.selection([('M', 'Male'),
                                     ('F', 'Female')
                                     ], 'Gender'),
        'marital': fields.selection([('single', 'Single'), 
                                     ('married', 'Married'), 
                                     ('widower', 'Widower'), 
                                     ('divorced', 'Divorced'),
                                     ], 'Marital Status'),
        'active': fields.boolean('Active', 
                                 help="If unchecked, it will allow you to hide the person without removing it."),
        }

    _defaults = {
        'date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': 1,
        }
    
    _sql_constraints = [('person_code_uniq', 'unique(code)', u'Error! The Person Code must be unique!')]

    _order='name'

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
            return {'value': {'person_phone': address.phone, 'mobile_phone': address.mobile, 'person_email': address.email}}
        return {'value': {}}
