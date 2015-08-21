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

class clv_medicament_dispensation(models.Model):
    _inherit = 'clv_medicament_dispensation'

    template_id = fields.Many2one('clv_medicament.template', string='Medicament Template', )

    @api.onchange('template_id')
    def _onchange_template_id(self):
        if self.template_id:
            self.prescriber_id = self.template_id.prescriber_id
            self.insured_card_id = self.template_id.insured_card_id

    @api.multi
    def write(self, vals):
        if ('prescriber_id' not in vals) and ('insured_card_id' not in vals):
            if 'template_id' in vals and vals['template_id'] != False:
                self.prescriber_id = self.template_id.prescriber_id
                self.insured_card_id = self.template_id.insured_card_id
        return super(clv_medicament_dispensation, self).write(vals)

class clv_medicament_template(models.Model):
    _inherit = 'clv_medicament.template'

    dispensation_ids = fields.One2many('clv_medicament_dispensation', 'template_id', string='Dispensations',)

