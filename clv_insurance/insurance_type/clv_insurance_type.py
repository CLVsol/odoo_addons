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


class clv_insurance_type (models.Model):
    _name = "clv_insurance.type"

    name = fields.Char('Insurance Type', size=128, help="Insurance Type")
    code = fields.Char('Insurance Type Code', size=32, help="Short name for the insurance type")
    description = fields.Text('Description')
    active = fields.Boolean('Active',
                            help="If unchecked, it will allow you to hide the insurance type without removing it.",
                            default=1)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Error! The Insurance Type name must be unique!'),
        ('code_uniq', 'unique (code)', 'Error! The Insurance Type code must be unique!')
        ]


class clv_insurance(models.Model):
    _inherit = 'clv_insurance'

    insurance_type_id = fields.Many2one('clv_insurance.type', 'Insurance Type', ondelete='restrict')
