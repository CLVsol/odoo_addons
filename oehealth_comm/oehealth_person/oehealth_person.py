# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2012  Carlos Eduardo Vercelino - CLVsol                        #
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

from osv import fields, osv
from datetime import datetime
from dateutil.relativedelta import relativedelta

class oehealth_person(osv.osv):
    _name = "oehealth.person"
    _table= "oehealth_person"
    _description = "Person"
    _inherits = {
                 'res.partner': "partner_id",
                 }

    def name_code_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name', 'person_code'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['person_code']:
                name = name + ' (' + record['person_code'][1] + ')'
            res.append((record['id'], name))
        return res

    def _name_code_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_code_get(cr, uid, ids, context=context)
        return dict(res)

    def _compute_age(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        now = datetime.now()
        for r in self.browse(cr, uid, ids, context=context):
            if r.birthday:
                dob = datetime.strptime(r.birthday,'%Y-%m-%d')
                delta=relativedelta (now, dob)
                #result[r.id] = str(delta.years) +"y "+ str(delta.months) +"m "+ str(delta.days)+"d" #if you only want date just give delta.years
                result[r.id] = str(delta.years)
            else:
                result[r.id] = "No Date of Birth!"
        return result

    _columns = {
        'partner_id': fields.many2one('res.partner', 'Related Partner', required=True,
                                     ondelete='cascade', help='Partner-related data of the Person'),
        #we need a related field in order to be able to sort the person by name
        'name_related': fields.related('partner_id', 'name', type='char', string='Related Partiner', 
                                       readonly=True, store=True),
        'alias' : fields.char('Alias', size=64, help='Common name that the Person is referred'),
        'name_code': fields.function(_name_code_get_fnc, type="char", string='Name (Code)'),
        'family_id': fields.many2one('oehealth.family', 
                                     string='Family',
                                     help='Family Name (Code)'),
        'country_id': fields.many2one('res.country', 'Nationality'),
        'birthday': fields.date("Date of Birth"),
        'age' : fields.function(_compute_age, method=True, type='char', size=32, string='Age',),
        #'birth_state_id': fields.many2one("res.country.state", 'Birth State', domain="[('country_id','=',birth_country_id)]"),
        #'birth_l10n_br_city_id': fields.many2one('l10n_br_base.city', 'Birth City', domain="[('state_id','=',birth_state_id)]"),
        'spouse_id': fields.many2one('oehealth.person', 'Spouse'),
        'father_id': fields.many2one('oehealth.person', 'Father'),
        'mother_id': fields.many2one('oehealth.person', 'Mother'),
        'responsible_id': fields.many2one('oehealth.person', 'Responsible'),
        'identification_id': fields.char('Person ID', size=10),
        'person_code': fields.many2one('oehealth.person.code', 'Person Code'),
        'otherid': fields.char('Other ID', size=64),
        'gender': fields.selection([('male', 'Male'),('female', 'Female')], 'Gender'),
        'marital': fields.selection([('single', 'Single'), ('married', 'Married'), ('widower', 'Widower'), ('divorced', 'Divorced')], 'Marital Status'),
        'community_area_id':fields.many2one('oehealth.comm_area', 'Community Area'),
        'notes': fields.text('Notes'),
        'category_ids': fields.many2many('oehealth.person.category', 
                                         id1='person_id', 
                                         id2='category_id', 
                                         string='Categories'),
        #'coach_id': fields.many2one('res.partner', 'Coach'),
        #'role_id': fields.many2one('oehealth.person.role', 'Role'),
        'color': fields.integer('Color Index'),
    }

    _order='name_related'

    def onchange_partner_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
            return {'value': {'work_phone': address.phone, 'mobile_phone': address.mobile}}
        return {'value': {}}

    _defaults = {
        'active': 1,
        'color': 0,
        'is_person': 1,
    }

    _sql_constraints = [
                        ('person_code_uniq', 'unique(person_code)', 'Person code already in use!'),
                        ]
    
class oehealth_comm_area(osv.osv):
    _description = "Community Area"
    _inherit = 'oehealth.comm_area'
    _columns = {
        'member_ids': fields.one2many('oehealth.person', 'community_area_id', 'Members', readonly=True),
    }

    def copy(self, cr, uid, ids, default=None, context=None):
        if default is None:
            default = {}
        default = default.copy()
        default['member_ids'] = []
        return super(oehealth_comm_area, self).copy(cr, uid, ids, default, context=context)
