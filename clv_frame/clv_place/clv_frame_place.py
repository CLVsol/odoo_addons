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
from datetime import *

class clv_frame_place(osv.Model):
    _name = 'clv_frame.place'

    _columns = {
        'place_id': fields.many2one('clv_place', 'Place', required=False),
        'frame_id': fields.many2one('clv_frame', string='Frame', help='Frame'),
        'sign_in_date': fields.datetime("Sign in date", required=False),
        'sign_out_date': fields.datetime("Sign out date", required=False),
        'notes': fields.text(string='Notes'),
        'active': fields.boolean('Active', help="If unchecked, it will allow you to hide the frame place without removing it."),
    }

    _order = "sign_in_date desc"

    _defaults = {
        'sign_in_date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': 1,
    }

class clv_frame(osv.osv):
    _inherit = 'clv_frame'

    _columns = {
        'place_ids': fields.one2many('clv_frame.place',
                                     'frame_id',
                                     'Places'),
    }

class clv_place(osv.osv):
    _inherit = 'clv_place'

    _columns = {
        'frame_ids': fields.one2many('clv_frame.place',
                                     'place_id',
                                     'Frames'),
    }
