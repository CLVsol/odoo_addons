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

    tag_ids = fields.Many2many('clv_tag', 
                               'clv_medicament_dispensation_ext_tag_rel', 
                               'medicament_dispensation_ext_id', 
                               'tag_id', 
                               'Tags')

class clv_tag(models.Model):
    _inherit = 'clv_tag'

    medicament_dispensation_ext_ids = fields.Many2many('clv_medicament_dispensation_ext', 
                                                       'clv_medicament_dispensation_ext_tag_rel', 
                                                       'tag_id', 
                                                       'medicament_dispensation_ext_id', 
                                                       'Dispensations (Ext)')
