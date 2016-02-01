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

from openerp import models, fields
from datetime import *


class clv_insurance(models.Model):
    _name = 'clv_insurance'

    name = fields.Char('Insurance', required=True, size=64, translate=False)
    alias = fields.Char('Alias', size=64, help='Common name that the Insurance is referred')
    code = fields.Char(size=64, string='Insurance Code', required=False)
    insurance_client_id = fields.Many2one('clv_insurance_client', 'Insurance Client', ondelete='restrict')
    notes = fields.Text(string='Notes')
    date_inclusion = fields.Date('Inclusion Date')
    active = fields.Boolean('Active',
                            help="If unchecked, it will allow you to hide the insurance without removing it.")

    _order = 'name'

    _sql_constraints = [('code_uniq', 'unique(code)', u'Error! The Insurance Code must be unique!')]

    _defaults = {
        'date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': 1,
        }
