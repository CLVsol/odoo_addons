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

class oehealth_medicament_mng(osv.Model):
    _name = 'oehealth.medicament_mng'
    _description = "Medicament Management"

    _columns = {
        'category_ids': fields.many2many('oehealth.medicament_mng.category', 
                                         'oehealth_medicament_mng_category_rel', 
                                         'medicament_mng_id', 
                                         'category_id', 
                                         'Categories'),
        'tag_ids': fields.many2many('oehealth.tag', 
                                    'oehealth_medicament_mng_tag_rel', 
                                    'medicament_mng_id', 
                                    'tag_id', 
                                    'Tags'),
        'state': fields.selection([('new','New'),
                                   ('revised','Revised'),
                                   ('processing','Processing'),
                                   ('okay','Okay')], 'Stage', readonly=True),

        'product_name': fields.char('Product Name', size=128, required=False, select=True),
        'name': fields.char('Name', size=128, required=False, select=True),
        'product_presentation': fields.char('Product/Presentation', size=128, required=False, select=True),
        'active_component_name': fields.char('Active Component', size=128, required=False, select=True),
        'concentration': fields.char(size=256, string='Concentration'),
        'presentation': fields.char(size=256, string='Presentation'),
        'pres2': fields.integer(string='Presentation Quantity'),
        'pres3': fields.char(size=256, string='Presentation Form'),
        'therap_class': fields.char(size=256, string='Therapeutic Class'),
        'manufacturer_name': fields.char('Medicament Manufacturer', size=128, required=False, select=True),
        'cod_prod': fields.integer(string='Cod. Produto GM', help='Código do Produto Garantemed'),
        'cod_abcfarma': fields.char(size=64, string='Cod. ABCFarma', help='Código ABCFarma'),
        'active': fields.boolean('Active', help="The active field allows you to hide the medicament without removing it."),
        'medicament': fields.many2one('oehealth.medicament', string='Medicament'),
        'price11': fields.float('Preço Cons. SP'),
        'price12': fields.float('Preço Fab. SP'),
        'price13': fields.float('Preço Rep. SP'),
        'therapeutic_class': fields.many2one('oehealth.medicament.therapeutic_class', string='Therapeutic Class', 
                                             help='Medicament Therapeutic Class'),
        'manufacturer': fields.many2one('oehealth.medicament.manufacturer', string='Manufacturer', 
                                        help='Medicament Manufacturer'),
    }

    _order='name'

    #_sql_constraints = [('medicament_mng_code_uniq', 'unique(medicament_mng_code)', u'Duplicated Medicament Management Code!')]

    _defaults = {
        'active': 1,
        'state': 'new',
    }
    
    def oehealth_medicament_mng_new(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'new'})
         return True

    def oehealth_medicament_mng_revised(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'revised'})
         return True

    def oehealth_medicament_mng_processing(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'processing'})
         return True

    def oehealth_medicament_mng_okay(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'okay'})
         return True

oehealth_medicament_mng()
