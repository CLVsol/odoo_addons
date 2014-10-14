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

from osv import osv
from osv import fields
import re
from datetime import datetime
from dateutil.relativedelta import relativedelta

def validate_cpf(cpf):

    if not cpf.isdigit():
        cpf = re.sub('[^0-9]', '', cpf)
    if len(cpf) != 11:
        return False
    cpf = map(int, cpf)
    new = cpf[:9]
    while len(new) < 11:
        r = sum([(len(new) + 1 - i) * v for i, v in enumerate(new)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        new.append(f)
    if new == cpf:
        return True
    return False

class oehealth_insured_mng(osv.Model):
    _name = 'oehealth.insured_mng'
    _description = "Health Insured Management"

    def _compute_age(self, cr, uid, ids, field_name, arg, context={}):
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
        'category_ids': fields.many2many('oehealth.insured_mng.category', 
                                         'oehealth_insured_mng_category_rel', 
                                         'insured_mng_id', 
                                         'category_id', 
                                         'Categories'),
        'tag_ids': fields.many2many('oehealth.tag', 
                                    'oehealth_insured_mng_tag_rel', 
                                    'insured_id', 
                                    'tag_id', 
                                    'Tags'),
        'state': fields.selection([('new','New'),
                                   ('revised','Revised'),
                                   ('processing','Processing'),
                                   ('okay','Okay')], 'Stage', readonly=True),



        'card_number': fields.char('Card Number', required=False, size=64, translate=False),
        'name': fields.char('Name', size=128, required=True, select=True),
        'alias' : fields.char('Alias', size=64, help='Common name that the Insured is referred'),
        'cpf': fields.char('CPF', size=14),
        'rg': fields.char('RG', size=16),
        'rg_emitter': fields.char('RG Emitter', size=16),
        'birthday': fields.date("Date of Birth"),
        'age' : fields.function(_compute_age, method=True, type='char', size=32, string='Age',),
        'identification_id': fields.char('Person ID', size=10),
        'otherid': fields.char('Other ID', size=64),
        'gender': fields.selection([('M', 'Male'),('F', 'Female')], 'Gender'),
        'marital': fields.selection([('single', 'Single'), 
                                     ('married', 'Married'), 
                                     ('widower', 'Widower'), 
                                     ('divorced', 'Divorced'),
                                     ], 'Marital Status'),
        'street': fields.char('Street', size=128),
        'street2': fields.char('Street2', size=128),
        'district': fields.char('Bairro', size=32),
        'number': fields.char('Number', size=10),
        'zip': fields.char('Zip', change_default=True, size=24),
        'city': fields.char('City', size=128),
        'country': fields.char('Country Name', size=64, help='The full name of the country.', required=False, translate=True),
        'country_state': fields.char('State Name', size=64, required=False, 
                                     help='Administrative divisions of a country. E.g. Fed. State, Departement, Canton'),
        'email': fields.char('Email', size=240),
        'phone': fields.char('Phone', size=64),
        'fax': fields.char('Fax', size=64),
        'mobile': fields.char('Mobile', size=64),



        'date_insured_card_inclusion' : fields.date('Insured Card Inclusion Date'),
        'date_insured_card_activation' : fields.date('Insured Card Activation Date'),
        'date_insured_card_inactivation' : fields.date('Insured Card Inactivation Date'),
        'date_insured_card_suspension' : fields.date('Insured Card Suspension Date'),
        'date_insured_card_expiration' : fields.date('Insured Card Expiration Date'),
        # 'insured_card_status': fields.selection([
        #                                          ('U', 'Undefined'),
        #                                          ('A', 'Activated'),
        #                                          ('I', 'Inactivated'),
        #                                          ('S', 'Suspended'),
        #                                          ('E', 'Expired'),
        #                                          ], string='Insured Card Status',
        #                                             select=True, sort=False, required=False, translate=True),
        'insured_card_status': fields.selection([('U', 'Undefined'),
                                                 ('A', 'Activated'),
                                                 ('I', 'Inactivated'),
                                                 ('S', 'Suspended'),
                                                 ('E', 'Expired'),
                                                 ], string='Insured Card Status', select=True, sort=False),
        'date_insured_inclusion' : fields.date('Insured Inclusion Date'),
        'date_insured_activation' : fields.date('Insured Activation Date'),
        'date_insured_inactivation' : fields.date('Insured Inactivation Date'),
        'date_insured_suspension' : fields.date('Insured Suspension Date'),
        # 'insured_status': fields.selection([('U', 'Undefined'),
        #                                     ('A', 'Activated'),
        #                                     ('I', 'Inactivated'),
        #                                     ('S', 'Suspended'),
        #                                     ], string='Insured Status',
        #                                        select=True, sort=False, required=False, translate=True),
        'insured_status': fields.selection([('U', 'Undefined'),
                                            ('A', 'Activated'),
                                            ('I', 'Inactivated'),
                                            ('S', 'Suspended'),
                                            ], string='Insured Status', select=True, sort=False),
        'date_patient_inclusion' : fields.date('Patient Inclusion Date'),
        'date_patient_activation' : fields.date('Patient Activation Date'),
        'date_patient_inactivation' : fields.date('Patient Inactivation Date'),
        # 'patient_status': fields.selection([('U', 'Undefined'),
        #                                     ('A', 'Activated'),
        #                                     ('I', 'Inactivated'),
        #                                     ], string='Patient Status',
        #                                        select=True, sort=False, required=False, translate=True),
        'patient_status': fields.selection([('U', 'Undefined'),
                                            ('A', 'Activated'),
                                            ('I', 'Inactivated'),
                                            ], string='Patient Status', select=True, sort=False),



        'insured_type': fields.selection([('T', 'Titular'),
        	                              ('D', 'Dependent'),
        	                              ('A', 'Aggregate')], 
        	                             'Insured Type'),
        'titular_card_number': fields.char('Titular Card Number', required=False, size=64, translate=False),
        'titular_name': fields.char('Titular Name', size=128, required=False),
        'titular_cpf': fields.char('Titular CPF', size=14),
        'kinship': fields.char('Kinship', size=32),

        'cod_oper': fields.integer(string='Cod. Operadora', help='Código da Operadora'),
        'cod_plan': fields.integer(string='Cod. Plano', help='Código do Plano'),
        'plan_name': fields.char('Plan Name', size=128),
        'client_name': fields.char('Client Name', size=128),

        'country_id': fields.many2one('res.country', 'Nationality'),
        'state_id': fields.many2one("res.country.state", 'State'),
        'l10n_br_city_id': fields.many2one('l10n_br_base.city', 'City',
                                           domain="[('state_id','=',state_id)]"),
        'insurance_client_id': fields.many2one('oehealth.insurance_client', 'Insurance Client'),
        'insurance_id': fields.many2one('oehealth.insurance', 'Insurance'),
        'client_id': fields.many2one('res.partner', 'Client (Partner)'),
        'company_id': fields.many2one('res.company', 'Client (Company)'),
        'insured_card': fields.many2one('oehealth.insured.card', 'Related Insured Card', required=False,
                                        help='Insured Card-related data of the insured'),
        'insured': fields.many2one('oehealth.insured', 'Related Insured', required=False,
                                   help='Insured-related data of the insured'),
        'titular_insured': fields.many2one('oehealth.insured', 'Titular Insured', required=False,
                                           help='Titular Insured-related data of the insured'),
        'patient': fields.many2one('oehealth.patient', 'Related Patient', required=False,
                                   help='Patient-related data of the insured'),
        'insured_group_id': fields.many2one('oehealth.insured.group', 'Insured Group'),
        'insured_group_member_id': fields.many2one('oehealth.insured.group.member', 'Insured Group Member'),
        'group_role_id': fields.many2one('oehealth.insured.group.member.role', 'Role'),
        'group_kinship_id': fields.many2one('oehealth.insured.group.member.kinship', 'Kinship', required=False),
        'active': fields.boolean('Active', help="The active field allows you to hide the insured without removing it."),
    }

    _order='name'

    _defaults = {
        'active': 1,
        'state': 'new',
    }
    
    def _check_cpf(self, cr, uid, ids):

        for insured in self.browse(cr, uid, ids):
            if not insured.cpf:
                continue
            if not validate_cpf(insured.cpf):
                return False
        return True

    _constraints = [(_check_cpf, 'CPF invalid!', ['cpf']),
                    (_check_cpf, 'Titular CPF invalid!', ['titular_cpf']),
                    ]

    def onchange_mask_cpf(self, cr, uid, ids, cpf):
        value = {}
        value['title'] = False
        domain = {'title': [('domain', '=', 'contact')]}
        result = {'value': value, 'domain': domain}
        if cpf:
            val = re.sub('[^0-9]', '', cpf)
            if len(val) == 11:
                cpf = "%s.%s.%s-%s" % (val[0:3], val[3:6], val[6:9], val[9:11])
            result['value'].update({'cpf': cpf})
        return result

    def onchange_mask_titular_cpf(self, cr, uid, ids, titular_cpf):
        value = {}
        value['title'] = False
        domain = {'title': [('domain', '=', 'contact')]}
        result = {'value': value, 'domain': domain}
        if cpf:
            val = re.sub('[^0-9]', '', titular_cpf)
            if len(val) == 11:
                titular_cpf = "%s.%s.%s-%s" % (val[0:3], val[3:6], val[6:9], val[9:11])
            result['value'].update({'titular_cpf': titular_cpf})
        return result

    def oehealth_insured_mng_new(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'new'})
         return True

    def oehealth_insured_mng_revised(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'revised'})
         return True

    def oehealth_insured_mng_processing(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'processing'})
         return True

    def oehealth_insured_mng_done(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'okay'})
         return True

oehealth_insured_mng()
