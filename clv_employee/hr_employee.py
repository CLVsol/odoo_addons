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


class hr_employee(models.Model):
    _inherit = 'hr.employee'

    code = fields.Char(size=64, string='Employee Code', required=False)

    _sql_constraints = [('code_uniq', 'unique(code)', u'Error! The Employee Code must be unique!')]

    @api.multi
    @api.depends('name', 'code')
    def name_get(self):
        result = []
        for employee in self:
            result.append((employee.id, '%s [%s]' % (employee.name, employee.code)))
        return result
