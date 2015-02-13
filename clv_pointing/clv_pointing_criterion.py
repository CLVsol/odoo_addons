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

class clv_pointing_criterion(models.Model):
    _name = "clv_pointing.criterion"

    name = fields.Char('Pointing', size=64)
    result = fields.Text('Result')
    # normal_range = fields.Text('Normal Range')
    # outcome_ids = fields.Many2many('clv_pointing.outcome', 
    #                                'clv_pointing_outcome_rel', 
    #                                'criterion_id', 
    #                                'outcome_id', 
    #                                'Outcomes')
    # valid_values = fields.Text('Valid Values')
    unit = fields.Many2one('clv_pointing.unit', 'Units')
    pointing_type_id = fields.Many2one('clv_pointing.type','Pointing Type')
    pointing_id = fields.Many2one('clv_pointing','Pointing Cases')
    sequence = fields.Integer('Sequence',
                              default=lambda *a : 10)       

    _order = "sequence"
