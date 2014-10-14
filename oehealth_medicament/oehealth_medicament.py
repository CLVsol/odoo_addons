# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2012  Carlos Eduardo Vercelino - CLVsol.net                    #
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

class oehealth_medicament (osv.osv):

    #def name_get(self, cr, uid, ids, context={}):
    #    if not len(ids):
    #        return []
    #    rec_name = 'name'
    #    result = [(r['id'], r[rec_name][1]) for r in self.read(cr, uid, ids, [rec_name], context)]
    #    return result

    _name = "oehealth.medicament"
    _inherits={
               'product.product': 'product_id',
               }

    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        reads = self.read(cr, uid, ids, ['name_active_component'], context=context)
        res = []
        for record in reads:
            name = record['name_active_component']
            res.append((record['id'], name))
        return res
    
    def name_active_component_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name', 'active_component'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['active_component']:
                #name = name + ' (' + record['active_component'][1] + ')'
                name = name + ' (' + record['active_component'] + ')'
            res.append((record['id'], name))
        return res

    def _name_active_component_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_active_component_get(cr, uid, ids, context=context)
        return dict(res)

    _columns = {
        #'name' : fields.many2one ('product.product', 'Name', domain=[('is_medicament', '=', True)], help="Commercial Name"),
        'name_product': fields.related('product_id', 'name', string="Name", type='char', size=128, store=True, select=True),
        'name_active_component': fields.function(_name_active_component_get_fnc, type="char", string='Name (Active Component)'),
        'product_id': fields.many2one('product.product', 'Related Product', required=True,
                                      ondelete='cascade', help='Product-related data of the medicament'),
        
        'active_component' : fields.char ('Active component', size=128, help="Active Component"),
        #'therapeutic_action' : fields.char ('Therapeutic effect', size=128, help="Therapeutic action"),
        #'composition' : fields.text ('Composition',help="Components"),
        #'indications' : fields.text ('Indication',help="Indications"),
        #'dosage' : fields.text ('Dosage Instructions',help="Dosage / Indications"),
        #'overdosage' : fields.text ('Overdosage',help="Overdosage"),
        #'pregnancy_warning' : fields.boolean ('Pregnancy Warning', help="Check when the drug can not be taken during pregnancy or lactancy"),
        #'pregnancy' : fields.text ('Pregnancy and Lactancy',help="Warnings for Pregnant Women"),
        #'presentation' : fields.text ('Presentation',help="Packaging"),
        #'adverse_reaction' : fields.text ('Adverse Reactions'),
        #'storage' : fields.text ('Storage Conditions'),
        #'price' : fields.related ('name','lst_price',type='float',string='Price'),
        #'qty_available' : fields.related ('name','qty_available',type='float',string='Quantity Available'),
        'notes' : fields.text ('Extra Info'),
        'category' : fields.many2one('oehealth.medicament.category', 'Category', help="Medicament Category")
        }
