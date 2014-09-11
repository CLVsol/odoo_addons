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
from datetime import *
from dateutil.relativedelta import relativedelta

class clv_batch(models.Model):
    _name = "clv_batch"

    name = fields.Char('Batch', required=True, size=64, translate=False)
    alias = fields.Char('Alias', size=64, help='Common name that the batch is referred')
    code = fields.Char(size=64, string='Batch Code', required=False)
    description = fields.Char(string='Description', size=256)
    size = fields.Integer(string='Size')
    parent_id = fields.Many2one('clv_batch', 'Parent Batch', select=True, ondelete='restrict')
    complete_name = fields.Char(string='Full Batch', compute='_name_get_fnc', store=False, readonly=True)
    child_ids = fields.One2many('clv_batch', 'parent_id', 'Child Batchs')
    item_birthday = fields.Date("Date of Birth")
    item_age = fields.Char(string='Item Age', size=32, compute='_item_age', store=False)
    is_movable = fields.Boolean('Is Movable', 
                                help="Check if the batch is movable, otherwise it is immovable",
                                default=False)
    batch_start = fields.Date("Batch Start",
                              default=lambda *a: datetime.now().strftime('%Y-%m-%d'))
    batch_age = fields.Char(string='Batch Age', size=32, compute='_batch_age', store=False)
    batch_end = fields.Date("Batch End")
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Datetime("Inclusion Date", required=False, readonly=False,
                                     default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    parent_left = fields.Integer('Left parent', select=True)
    parent_right = fields.Integer('Right parent', select=True)
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the batch without removing it.",
                            default=1)
    origin_batch_ids = fields.Many2many('clv_batch', 
                                        'clv_batch_origin_rel', 
                                        'to_batch_id', 
                                        'from_batch_id', 
                                        'Origin Batches')
    derived_batch_ids = fields.Many2many('clv_batch', 
                                         'clv_batch_origin_rel', 
                                         'from_batch_id', 
                                         'to_batch_id', 
                                         'Derived Batches')

    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'

    _constraints = [
        (osv.osv._check_recursion, 'Error! You can not create recursive batches.', ['parent_id'])
        ]

    _sql_constraints = [
                        ('uniq_code', 'unique(code)', "The Batch Code must be unique!"),
                        ]

    @api.multi
    def name_get(self):
        """Return the batch's display name, including their direct parent by default.

        :param dict context: the ``batch_display`` key can be
                             used to select the short version of the
                             batch (without the direct parent),
                             when set to ``'short'``. The default is
                             the long version."""
        if self._context is None:
            self._context = {}
        if self._context.get('batch_display') == 'short':
            return super(clv_batch, self).name_get()
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
            # Be sure name_search is symetric to name_get
            name = name.split(' / ')[-1]
            args = [('name', operator, name)] + args
        batches = self.search(args, limit=limit)
        return batches.name_get()

    @api.one
    def _name_get_fnc(self):
        self.refresh_complete_name = 0
        complete_name =  self.name_get()
        if complete_name:
            self.complete_name = complete_name[0][1]
        else:
            self.complete_name = self.name

    @api.one
    @api.depends('item_birthday')
    def _item_age(self):
        now = datetime.now()
        if self.item_birthday:
            dob = datetime.strptime(self.item_birthday,'%Y-%m-%d')
            delta=relativedelta (now, dob)
            self.item_age = str(delta.years) +"y "+ str(delta.months) +"m "+ str(delta.days)+"d"
        else:
            self.item_age = "No Item Date of Birth!"

    @api.one
    @api.depends('batch_start')
    def _batch_age(self):
        now = datetime.now()
        if self.batch_start:
            dob = datetime.strptime(self.batch_start,'%Y-%m-%d')
            delta=relativedelta (now, dob)
            self.batch_age = str(delta.years) +"y "+ str(delta.months) +"m "+ str(delta.days)+"d"
        else:
            self.batch_age = "No Item Date of Birth!"
