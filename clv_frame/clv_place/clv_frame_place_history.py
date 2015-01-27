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
from openerp.osv import osv
from datetime import *

class clv_frame_place_history(osv.Model):
    _name = 'clv_frame.place_history'

    frame_id = fields.Many2one('clv_frame', 'Frame', required=False)
    place_id = fields.Many2one('clv_place', 'Place', required=False)
    incoming_date = fields.Datetime('Incoming Date', required=False,
                                    default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    outgoing_date = fields.Datetime('Outgoing Date', required=False)
    notes = fields.Text(string='Notes')
    
    _order = "incoming_date desc"

class clv_frame(osv.Model):
    _inherit = 'clv_frame'

    place_history_ids = fields.One2many('clv_frame.place_history', 'frame_id', 'Place History')

class clv_place(osv.Model):
    _inherit = 'clv_place'

    frame_place_history_ids = fields.One2many('clv_frame.place_history', 'place_id', 'Frame Place History')
