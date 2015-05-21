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

class clv_medicament_mng(osv.osv):
    _name = 'clv_medicament_mng'

    _columns = {
        'product_name': fields.char('Product Name', size=128, required=False, select=True),
        # 'medicament_name': fields.char(size=256, string='Name'),
        'name': fields.char('Name', size=256, required=False, select=True),
        # 'code': fields.char(size=64, string='Medicament Code', required=False),
        'product_presentation': fields.char('Product/Presentation', size=128, required=False, select=True),
        'active_component_name': fields.char('Active Component', size=128, required=False, select=True),
        'concentration': fields.char(size=256, string='Concentration'),
        'presentation': fields.char(size=256, string='Presentation'),
        'pres_form': fields.many2one('clv_medicament.form', string='Presentation Form', 
                                     help='Medicament form, such as tablet or gel'),
        'pres_form_2': fields.many2one('clv_medicament.form', string='Presentation Form 2', 
                                        help='Medicament form, such as tablet or gel'),
        'pres_quantity': fields.integer(string='Presentation Quantity'),
        'pres_quantity_unit': fields.many2one('clv_medicament.uom', string='Quantity Unit', 
                                              help='Unit of measure for the medicament to be taken'),
        'therap_class': fields.char(size=256, string='Therapeutic Class'),
        'manufacturer_name': fields.char('Medicament Manufacturer', size=128, required=False, select=True),
        # 'medicament': fields.many2one('clv_medicament', string='Medicament'),
        # 'therapeutic_class': fields.many2one('clv_medicament.therapeutic_class', string='Therapeutic Class', 
        #                                      help='Medicament Therapeutic Class'),
        # 'manufacturer': fields.many2one('clv_medicament.manufacturer', string='Manufacturer', 
        #                                 help='Medicament Manufacturer'),
        'composition': fields.text(string='Composition', help='Components'),
        'ean13': fields.char('EAN13 Barcode', size=13, help="International Article Number used for product identification."),
        'notes': fields.text(string='Notes'),
        'date_inclusion': fields.datetime("Inclusion Date", required=False, readonly=False),
        'active': fields.boolean('Active', 
                                 help="If unchecked, it will allow you to hide the medicament without removing it."),
        'is_fraction': fields.boolean('Is a Fraction', 
                                      help="Check if the medicament is a fraction of a product."),
        }

    _order='product_name'

    # _sql_constraints = [('code_uniq', 'unique(code)', u'Error! The Medicament Code must be unique!')]

    _defaults = {
        'active': 1,
        'date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'is_fraction': False,
        }
    