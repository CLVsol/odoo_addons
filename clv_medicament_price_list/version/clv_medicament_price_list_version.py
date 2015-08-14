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

class clv_medicament_price_list_version(models.Model):
    _name = 'clv_medicament_price_list.version'

    # def name_get(self, cr, uid, ids, context={}):
    #     if not len(ids):
    #         return []
    #     reads = self.read(cr, uid, ids, ['name', 'catalog_name'], context=context)
    #     res = []
    #     for record in reads:
    #         name = record['name']
    #         if record['catalog_name']:
    #             name = record['catalog_name'] + ', ' + name
    #         res.append((record['id'], name))
    #     return res
    
    list_id = fields.Many2one('clv_medicament_price_list', 'Medicament Price List')
    name = fields.Char('Price List Version', required=True, size=64)
    # complete_name = fields.Char(string='Full Name', compute='_name_get_fnc', store=False, readonly=True)
    code = fields.Char ('Price List Version Code',size=128, required=False)
    description = fields.Char(string='Description', size=256)
    notes = fields.Text(string='Notes')
    active = fields.Boolean('Active', 
                            help='The active field allows you to hide the list version without removing it.',
                            default=1)

    _sql_constraints = [
        # ('uniq_list_name', 'unique(name)', "Error! The List Version Name must be unique!"),
        ('uniq_list_code', 'unique(code)', "Error! The Price List Version Code must be unique!"),
        ]

    @api.multi
    def name_get(self):
        """Return the version's display name, including their direct list by default.

        :param dict context: the ``version_display`` key can be
                             used to select the short version of the
                             version (without the direct list),
                             when set to ``'short'``. The default is
                             the long version."""
        if self._context is None:
            self._context = {}
        if self._context.get('version_display') == 'short':
            return super(clv_version, self).name_get()
        if isinstance(self._ids, (int, long)):
            self._ids = [self._ids]
        reads = self.read(['name', 'list_id'])
        res = []
        for record in reads:
            name = record['name']
            if record['list_id']:
                name = record['list_id'][1] + ' / ' + name
            res.append((record['id'], name))
        return res

class clv_medicament_price_list(models.Model):
    _inherit = 'clv_medicament_price_list'

    current_version_id = fields.Many2one('clv_medicament_price_list.version', 'Current Price List Version', 
                                         domain="[('list_id','=',id)]")
    medicament_price_list_version_ids = fields.One2many('clv_medicament_price_list.version',
                                                        'list_id',
                                                        'Medicament Price List Versions')
