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

class clv_lab_test_unit(models.Model):
    _name = "clv_lab_test.unit"

    name = fields.Char('Unit', required=True, size=25)
    code = fields.Char('Code', size=25)
    description = fields.Text ('Description')
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the unit without removing it.",
                            default=1)

    _sql_constraints = [('name_uniq', 'unique(name)', 'Error. The Unit name must be unique!'),
                        ('code_uniq', 'unique(code)', 'Error. The Unit code must be unique')
                        ]
