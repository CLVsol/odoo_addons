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

from openerp.osv import fields, osv

class clv_batch_placement_frame(osv.Model):
    _name = 'clv_batch.placement.frame'

    _columns = {
        'name': fields.many2one('clv_frame', 'Frame', required=True),
        'batch_placement_id': fields.many2one('clv_batch.placement', string='Batch Placement', help='Batch Placement'),
        'notes': fields.text(string='Notes'),
        'active': fields.boolean('Active', help="If unchecked, it will allow you to hide the placement frame without removing it."),
    }

    _defaults = {
        'active': 1,
    }

class clv_batch_placement(osv.osv):
    _inherit = 'clv_batch.placement'

    _columns = {
        'frame_ids': fields.one2many('clv_batch.placement.frame',
                                     'batch_placement_id',
                                     'Frames'),
    }

class oebase_clv_frame(osv.Model):
    _inherit = 'clv_frame'

    _columns = {
        'clv_batch_placement_frame_ids': fields.one2many('clv_batch.placement.frame', 'name', 'Batch Placements'),
    }
