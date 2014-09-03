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

class clv_lab_test_outcome(models.Model):
    _name = 'clv_lab_test.outcome'

    name = fields.Char('Lab Test Outcome', required=True, size=64, translate=True)
    description = fields.Text(string='Description')
    info = fields.Text(string='Info')
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the outcome without removing it.",
                            default=1)

    _order = 'name'
