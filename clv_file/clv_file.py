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
from datetime import *

class clv_file(models.Model):
    _name = 'clv_file'

    name = fields.Char('Name', required=True, size=128, translate=False)
    alias = fields.Char('Alias', size=64, help='Common name that the file is referred')
    code = fields.Char(size=64, string='File Code', required=False)
    path = fields.Char(string='Path', compute='_compute_path_str', store=False, readonly=True)
    description = fields.Text(string='Description', translate=False)
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Datetime('Inclusion Date',
                                     default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the file without removing it.",
                            default=1)
    url = fields.Char('URL', size=256, help="URL of the File")
    ct_url =fields.Char('Connected Text URL', 
                        size=256, 
                        help="Connected Text URL of the File")
    parent_id = fields.Many2one('clv_file', 'Parent File')
    child_ids = fields.One2many('clv_file', 'parent_id', 'Child Files')

    _order='name'

    _sql_constraints = [('code_uniq', 'unique(code)', u'Duplicated File Code!')]

    @api.one
    def _compute_path_str(self):
        if self.alias:
            self.path = self.alias + '_' + self.code + '_'
        else:
            self.path = '_' + self.code + '_'
