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

class clv_insured_mng(models.Model):
    _inherit = 'clv_insured_mng'

    insurance_client_id = fields.Many2one('clv_insurance_client', 'Insurance Client')
    reg_number = fields.Char('Reg. Number', size=32)

    @api.multi
    @api.depends('name', 'insurance_client_id')
    def name_get(self):
        result = []
        for insured in self:
            if insured.insurance_client_id:
                result.append((insured.id, '%s, %s' % (insured.insurance_client_id.name, insured.name)))
            else:
                result.append((insured.id, '%s' % (insured.name)))
        return result

