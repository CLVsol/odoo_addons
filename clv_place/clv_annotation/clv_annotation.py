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

class clv_place(models.Model):
    _inherit = 'clv_place'

    annotation_ids = fields.Many2many('clv_annotation', 
                                      'clv_place_annotation_rel', 
                                      'place_id', 
                                      'annotation_id', 
                                      'Annotations')

class clv_annotation(models.Model):
    _inherit = 'clv_annotation'

    place_ids = fields.Many2many('clv_place', 
                                 'clv_place_annotation_rel', 
                                 'annotation_id', 
                                 'place_id', 
                                 'Places')
