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

class clv_medicament_dispensation_ext(models.Model):
    _inherit = 'clv_medicament_dispensation_ext'

    dispensation_id = fields.Many2one('clv_medicament_dispensation',
                                      string='Dispensation')

    @api.onchange('dispensation_id')
    def _onchange_dispensation_id(self):
        disp = self.env['clv_medicament_dispensation'].search([('id', '=', self.dispens.id)])
        disp_ext = self.env['clv_medicament_dispensation_ext'].search([('name', '=', self.name)])
        disp.write({'disp_ext_id': disp_ext.id})

class clv_medicament_dispensation(models.Model):
    _inherit = 'clv_medicament_dispensation'

    dispensation_ext_id = fields.Many2one('clv_medicament_dispensation_ext',
                                          string='Dispensation (Ext)')
