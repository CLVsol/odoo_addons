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

class clv_family_person_role(models.Model):
    _name = 'clv_family.person_role'

    name = fields.Char(size=256, 
                       string='Family Person Role', required=True, 
                       help='Role of a Person in an Family')
    description = fields.Text(string='Description')
    notes = fields.Text(string='Notes')
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the role without removing it.",
                            default=1)
    _order='name'

    _sql_constraints = [('role_name_uniq', 'unique(name)', 
                         u'Error! The Role Name must be unique!')]
