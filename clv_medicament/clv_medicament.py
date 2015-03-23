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

class clv_medicament(osv.osv):
    _name = 'clv_medicament'
    _inherits={
        'product.product': 'product_id',
        }

    _columns = {
        'product_id': fields.many2one('product.product', 'Product', required=True,
                                      ondelete='cascade', help='Product-related data of the medicament'),
        #we need a related field in order to be able to sort the medicament by name
        'name_product': fields.related('product_id', 'name', type='char', string='Related Product', 
                                       readonly=True, store=True),
        'code': fields.char(size=64, string='Medicament Code', required=False),
        'medicament_name': fields.char(size=256, string='Name'),
        'concentration': fields.char(size=256, string='Concentration'),
        'presentation': fields.char(size=256, string='Presentation'),
        'pres_quantity': fields.integer(string='Presentation Quantity'),
        'pres_form': fields.char(size=256, string='Presentation Form'),
        'composition': fields.text(string='Composition', help='Components'),
        # 'indications': fields.text(string='Indication', help='Indications'),
        # 'therapeutic_action': fields.char(size=256,
        #                                   string='Therapeutic effect', 
        #                                   help='Therapeutic action'),
        # 'pregnancy_category': fields.selection([('A', 'A'),
        #                                         ('B', 'B'),
        #                                         ('C', 'C'),
        #                                         ('D', 'D'),
        #                                         ('X', 'X'),
        #                                         ('N', 'N'),
        #                                         ], string='Pregnancy Category', 
        #                                        help='** FDA Pregancy Categories ***\n'\
        #                                             'CATEGORY A :Adequate and well-controlled human studies have failed'\
        #                                             ' to demonstrate a risk to the fetus in the first trimester of'\
        #                                             ' pregnancy (and there is no evidence of risk in later'\
        #                                             ' trimesters).\n\n'\
        #                                             'CATEGORY B : Animal reproduction studies have failed todemonstrate a'\
        #                                             ' risk to the fetus and there are no adequate and well-controlled'\
        #                                             ' studies in pregnant women OR Animal studies have shown an adverse'\
        #                                             ' effect, but adequate and well-controlled studies in pregnant women'\
        #                                             ' have failed to demonstrate a risk to the fetus in any'\
        #                                             ' trimester.\n\n'
        #                                             'CATEGORY C : Animal reproduction studies have shown an adverse'\
        #                                             ' effect on the fetus and there are no adequate and well-controlled'\
        #                                             ' studies in humans, but potential benefits may warrant use of the'\
        #                                             ' drug in pregnant women despite potential risks. \n\n '\
        #                                             'CATEGORY D : There is positive evidence of human fetal  risk based'\
        #                                             ' on adverse reaction data from investigational or marketing'\
        #                                             ' experience or studies in humans, but potential benefits may warrant'\
        #                                             ' use of the drug in pregnant women despite potential risks.\n\n'\
        #                                             'CATEGORY X : Studies in animals or humans have demonstrated fetal'\
        #                                             ' abnormalities and/or there is positive evidence of human fetal risk'\
        #                                             ' based on adverse reaction data from investigational or marketing'\
        #                                             ' experience, and the risks involved in use of the drug in pregnant'\
        #                                             ' women clearly outweigh potential benefits.\n\n'\
        #                                             'CATEGORY N : Not yet classified'),
        # 'overdosage': fields.text(string='Overdosage', help='Overdosage'),
        # 'pregnancy_warning': fields.boolean(string='Pregnancy Warning', 
        #                                     help='The drug represents risk to pregnancy or lactancy'),
        'notes': fields.text(string='Notes'),
        # 'storage': fields.text(string='Storage Conditions'),
        # 'adverse_reaction': fields.text(string='Adverse Reactions'),
        # 'dosage': fields.text(string='Dosage Instructions', 
        #                       help='Dosage / Indications'),
        # 'pregnancy': fields.text(string='Pregnancy and Lactancy', 
        #                          help='Warnings for Pregnant Women'),
        'date_inclusion': fields.datetime("Inclusion Date", required=False, readonly=False),
        # 'date_medicament_inclusion' : fields.date('Medicament Inclusion Date'),
        # 'date_medicament_activation' : fields.date('Medicament Activation Date'),
        # 'date_medicament_inactivation' : fields.date('Medicament Inactivation Date'),
        # 'date_medicament_suspension' : fields.date('Medicament Suspension Date'),
        # 'medicament_rgss': fields.selection([('U', 'Undefined'),
        #                                      ('R', 'Reference'),
        #                                      ('G', 'Generic'),
        #                                      ('S', 'Similar'),
        #                                      ], string='Medicament Status',
        #                                           select=True, sort=False, required=False, translate=True),
        'therapeutic_class': fields.many2one('clv_medicament.therapeutic_class', string='Therapeutic Class', 
                                             help='Medicament Therapeutic Class'),
        'manufacturer': fields.many2one('clv_medicament.manufacturer', string='Manufacturer', 
                                        help='Medicament Manufacturer'),
        }

    _order='name_product'

    _sql_constraints = [('code_uniq', 'unique(code)', u'Error! The Medicament Code must be unique!')]

    _defaults = {
        'active': 1,
        'is_medicament': True,
        'date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }
    