# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2012  Carlos Vercelino - CLVsol.net                            #
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

class health_medicament_category(osv.osv):

    def name_get(self, cr, uid, ids, context=None):
        if isinstance(ids, (list, tuple)) and not len(ids):
            return []
        if isinstance(ids, (long, int)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name','parent_id'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['parent_id']:
                name = record['parent_id'][1]+' / '+name
            res.append((record['id'], name))
        return res

    def _name_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_get(cr, uid, ids, context=context)
        return dict(res)

    _name = "health.medicament.category"
    _description = "Health Medicament Category"
    _columns = {
        'name': fields.char('Name', size=64, required=True, translate=True, select=True),
        'complete_name': fields.function(_name_get_fnc, type="char", string='Name'),
        'parent_id': fields.many2one('health.medicament.category','Parent Category', select=True, ondelete='cascade'),
        'child_id': fields.one2many('health.medicament.category', 'parent_id', string='Child Categories'),
        'sequence': fields.integer('Sequence', select=True, help="Gives the sequence order when displaying a catalog of product categories."),
        'type': fields.selection([('view','View'), ('normal','Normal')], 'Category Type', help="A category of the view type is a virtual category that can be used as the parent of another category to create a hierarchical structure."),
        'parent_left': fields.integer('Left Parent', select=1),
        'parent_right': fields.integer('Right Parent', select=1),
    }


    _defaults = {
        'type' : lambda *a : 'normal',
    }

    _parent_name = "parent_id"
    _parent_store = True
    _parent_order = 'sequence, name'
    _order = 'parent_left'

    def _check_recursion(self, cr, uid, ids, context=None):
        level = 100
        while len(ids):
            cr.execute('select distinct parent_id from product_category where id IN %s',(tuple(ids),))
            ids = filter(None, map(lambda x:x[0], cr.fetchall()))
            if not level:
                return False
            level -= 1
        return True

    _constraints = [
        (_check_recursion, 'Error ! You cannot create recursive categories.', ['parent_id'])
    ]
    def child_get(self, cr, uid, ids):
        return [ids]

class health_medicament_catalog(osv.osv):

    def name_get(self, cr, uid, ids, context=None):
        """Return the catalogs' display name, including their direct
           parent by default.

        :param dict context: the ``medicament_catalog_display`` key can be
                             used to select the short version of the
                             catalog name (without the direct parent),
                             when set to ``'short'``. The default is
                             the long version."""
        if context is None:
            context = {}
        if context.get('medicament_catalog_display') == 'short':
            return super(health_medicament_catalog, self).name_get(cr, uid, ids, context=context)
        if isinstance(ids, (int, long)):
            ids = [ids]
        reads = self.read(cr, uid, ids, ['name', 'parent_id'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['parent_id']:
                name = record['parent_id'][1] + ' / ' + name
            res.append((record['id'], name))
        return res

    def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=100):
        if not args:
            args = []
        if not context:
            context = {}
        if name:
            # Be sure name_search is symetric to name_get
            name = name.split(' / ')[-1]
            ids = self.search(cr, uid, [('name', operator, name)] + args, limit=limit, context=context)
        else:
            ids = self.search(cr, uid, args, limit=limit, context=context)
        return self.name_get(cr, uid, ids, context)


    def _name_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_get(cr, uid, ids, context=context)
        return dict(res)

    _description = 'Health Medicament Catalogs'
    _name = 'health.medicament.catalog'
    _columns = {
        'name': fields.char('Medicament Catalog Name', required=True, size=64, translate=True),
        'parent_id': fields.many2one('health.medicament.catalog', 'Parent Medicament Catalog', select=True, ondelete='cascade'),
        'complete_name': fields.function(_name_get_fnc, type="char", string='Full Name'),
        'child_ids': fields.one2many('health.medicament.catalog', 'parent_id', 'Child Medicament Catalogs'),
        'active': fields.boolean('Active', help="The active field allows you to hide the medicament catalog without removing it."),
        'parent_left': fields.integer('Left parent', select=True),
        'parent_right': fields.integer('Right parent', select=True),
        'medicament_ids': fields.many2many('health.medicament', id1='catalog_id', id2='medicament_id', string='Medicaments'),
    }
    _constraints = [
        (osv.osv._check_recursion, 'Error ! You can not create recursive catalogs.', ['parent_id'])
    ]
    _defaults = {
        'active': 1,
    }
    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'

class health_medicament (osv.osv):

    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        rec_name = 'name'
        result = [(r['id'], r[rec_name][1]) for r in self.read(cr, uid, ids, [rec_name], context)]
        return result

    _name = "health.medicament"
    _columns = {
        'name' : fields.many2one ('product.product', 'Name', domain=[('is_medicament', '=', True)], help="Commercial Name"),
        'active_component' : fields.char ('Active component', size=128, help="Active Component"),
        'therapeutic_action' : fields.char ('Therapeutic effect', size=128, help="Therapeutic action"),
        'composition' : fields.text ('Composition',help="Components"),
        'indications' : fields.text ('Indication',help="Indications"),
        'dosage' : fields.text ('Dosage Instructions',help="Dosage / Indications"),
        'overdosage' : fields.text ('Overdosage',help="Overdosage"),
        'pregnancy_warning' : fields.boolean ('Pregnancy Warning', help="Check when the drug can not be taken during pregnancy or lactancy"),
        'pregnancy' : fields.text ('Pregnancy and Lactancy',help="Warnings for Pregnant Women"),
        'presentation' : fields.text ('Presentation',help="Packaging"),
        'adverse_reaction' : fields.text ('Adverse Reactions'),
        'storage' : fields.text ('Storage Conditions'),
        'price' : fields.related ('name','lst_price',type='float',string='Price'),
        'qty_available' : fields.related ('name','qty_available',type='float',string='Quantity Available'),
        'notes' : fields.text ('Extra Info'),
        'category' : fields.many2one('health.medicament.category', 'Category', help="Medicament Category")
        }
