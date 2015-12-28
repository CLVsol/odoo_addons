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


class clv_community_family(osv.osv):
    _name = 'clv_community.family'

    _columns = {
        'community_id': fields.many2one('clv_community', string='Community',
                                        help='Community', required=False),
        'family_id': fields.many2one('clv_family', string='Family'),
        'role': fields.many2one('clv_community.family_role', 'Role', required=False),
        'notes': fields.text(string='Notes'),
        'active': fields.boolean('Active',
                                 help="If unchecked, it will allow you to hide the family without removing it."),
        }

    _defaults = {
        'active': 1,
        }


class clv_community(osv.osv):
    _inherit = 'clv_community'

    _columns = {
        'family_ids': fields.one2many('clv_community.family',
                                      'community_id',
                                      'Families'),
    }


class clv_family(osv.osv):
    _inherit = 'clv_family'

    _columns = {
        'community_ids': fields.one2many('clv_community.family',
                                         'family_id',
                                         'Community Roles'),
        }
