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

# from openerp.osv import fields, osv
# from datetime import datetime
# from dateutil.relativedelta import relativedelta

#class clv_frame(osv.osv):
class clv_frame(models.Model):
    _name = "clv_frame"

    name = fields.Char('Frame', required=True, size=64, translate=False)
    alias = fields.Char('Alias', size=64, help='Common name that the frame is referred')
    code = fields.Char(size=64, string='Frame Code', required=False)
    description = fields.Char(string='Description', size=256)
    parent_id = fields.Many2one('clv_frame', 'Parent Frame', select=True, ondelete='restrict')
    complete_name = fields.Char(string='Full Frame', compute='_name_get_fnc', store=False, readonly=True)
    child_ids = fields.One2many('clv_frame', 'parent_id', 'Child Frames')
    is_movable = fields.Boolean('Is Movable', 
                                help="Check if the frame is movable, otherwise it is immovable",
                                default=False)
    address_id = fields.Many2one('res.partner', 'Frame Address')
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Datetime("Inclusion Date", required=False, readonly=False,
                                     default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    parent_left = fields.Integer('Left parent', select=True)
    parent_right = fields.Integer('Right parent', select=True)
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the frame without removing it.",
                            default=1)
    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'

    _sql_constraints = [('frame_code_uniq', 'unique(frame_code)', u'Duplicated Frame Code!')]

    _constraints = [
        (osv.osv._check_recursion, 'Error! You can not create recursive frames.', ['parent_id'])
        ]

    @api.multi
    def name_get(self):
        """Return the frame's display name, including their direct parent by default.

        :param dict context: the ``frame_display`` key can be
                             used to select the short version of the
                             frame (without the direct parent),
                             when set to ``'short'``. The default is
                             the long version."""
        if self._context is None:
            self._context = {}
        if self._context.get('frame_display') == 'short':
            return super(clv_frame, self).name_get()
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
        frames = self.search(args, limit=limit)
        return frames.name_get()

    @api.one
    def _name_get_fnc(self):
        self.refresh_complete_name = 0
        complete_name =  self.name_get()
        if complete_name:
            self.complete_name = complete_name[0][1]
        else:
            self.complete_name = self.name

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        if address:
            address = self.pool.get('res.partner').browse(cr, uid, address, context=context)
            return {'value': {'comm_phone': address.phone, 'mobile_phone': address.mobile}}
        return {'value': {}}

