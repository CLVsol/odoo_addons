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

class clv_lab_test_type (models.Model):
    _name = "clv_lab_test.type"

    name = fields.Char ('Test',size=128, help="Test type, eg X-Ray, hemogram, biopsy...")
    code = fields.Char ('Code',size=32, help="Short name - code for the test")
    info = fields.Text ('Description')
    # product_id = fields.Many2one('product.product', 'Service', required=True)
    product_id = fields.Many2one('product.product', 'Service', required=False)
    criteria = fields.One2many('clv_lab_test.criterion','lab_test_type_id','Test Cases')

    _sql_constraints = [
    	('name_uniq', 'unique (name)', 'The Lab Test name must be unique'),
        ('code_uniq', 'unique (code)', 'The Lab Test code must be unique')
        ]
