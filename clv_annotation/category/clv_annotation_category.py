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
from openerp.osv import osv

class clv_annotation_category(models.Model):
    _name = 'clv_annotation.category'

    name = fields.Char('Category', required=True, size=64, translate=True)
    parent_id = fields.Many2one('clv_annotation.category', 'Parent Category', select=True, ondelete='restrict')
    code = fields.Char ('Category Code',size=128, required=False)
    description = fields.Char(string='Description', size=256)
    notes = fields.Text(string='Notes')
    complete_name = fields.Char(string='Full Category', compute='_name_get_fnc', store=False, readonly=True)
    child_ids = fields.One2many('clv_annotation.category', 'parent_id', 'Child Categories')
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the category without removing it.",
                            default=1)
    parent_left = fields.Integer('Left parent', select=True)
    parent_right = fields.Integer('Right parent', select=True)
    annotation_ids = fields.Many2many('clv_annotation', 
                                      'clv_annotation_category_rel', 
                                      'category_id', 
                                      'annotation_id', 
                                      'Annotations')

    _sql_constraints = [
        ('uniq_category_code', 'unique(code)', "Error! The Category Code must be unique!"),
        ]

    _constraints = [
        (models.Model._check_recursion, 'Error! You can not create recursive categories.', ['parent_id'])
        ]
    
    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'

    @api.multi
    def name_get(self):
        """Return the category's display name, including their direct parent by default.

        :param dict context: the ``category_display`` key can be
                             used to select the short version of the
                             category (without the direct parent),
                             when set to ``'short'``. The default is
                             the long version."""
        if self._context is None:
            self._context = {}
        if self._context.get('category_display') == 'short':
            return super(clv_category, self).name_get()
        if isinstance(self._ids, (int, long)):
            self._ids = [self._ids]
        reads = self.read(['name', 'parent_id'])
        res = []
        for record in reads:
            name = record['name']
            if record['parent_id']:
                name = record['parent_id'][1] + ' / ' + name
            res.append((record['id'], name))
        return res

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            name = name.split(' / ')[-1]
            args = [('name', operator, name)] + args
        categories = self.search(args, limit=limit)
        return categories.name_get()


    @api.multi
    def _name_get_fnc(self, field_name, arg):
        return dict(self.name_get())

    @api.one
    def _name_get_fnc(self):
        self.refresh_complete_name = 0
        complete_name =  self.name_get()
        if complete_name:
            self.complete_name = complete_name[0][1]
        else:
            self.complete_name = self.name

class clv_annotation(models.Model):
    _inherit = 'clv_annotation'

    category_ids = fields.Many2many('clv_annotation.category', 
                                    'clv_annotation_category_rel', 
                                    'annotation_id', 
                                    'category_id', 
                                    'Categories')
