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

class clv_pointing_type (models.Model):
    _name = "clv_pointing.type"

    name = fields.Char('Pointing Type', size=128, help="Pointing type")
    code = fields.Char('Code',size=32, help="Short name - code for the pointing")
    description = fields.Text('Description')
    criteria = fields.One2many('clv_pointing.criterion','pointing_type_id','Pointing Cases')

    _sql_constraints = [
    	('name_uniq', 'unique (name)', 'The Pointing name must be unique'),
        ('code_uniq', 'unique (code)', 'The Pointing code must be unique')
        ]
