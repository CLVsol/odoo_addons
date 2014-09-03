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

class clv_frame(models.Model):
    _inherit = 'clv_frame'

    tag_ids = fields.Many2many('clv_tag', 
                               'clv_frame_tag_rel', 
                               'frame_id', 
                               'tag_id', 
                               'Tags')

class clv_tag(models.Model):
    _inherit = 'clv_tag'

    frame_ids = fields.Many2many('clv_frame', 
                                 'clv_frame_tag_rel', 
                                 'tag_id', 
                                 'frame_id', 
                                 'Frames')
