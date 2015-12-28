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


class clv_community_person(osv.osv):
    _name = 'clv_community.person'

    _columns = {
        'community_id': fields.many2one('clv_community', string='Community',
                                        help='Community', required=False),
        'person_id': fields.many2one('clv_person', string='Person'),
        'role': fields.many2one('clv_community.person_role', 'Role', required=False),
        'notes': fields.text(string='Notes'),
        'active': fields.boolean('Active',
                                 help="If unchecked, it will allow you to hide the person without removing it."),
        }

    _defaults = {
        'active': 1,
        }


class clv_community(osv.osv):
    _inherit = 'clv_community'

    _columns = {
        'person_ids': fields.one2many('clv_community.person',
                                      'community_id',
                                      'Persons'),
    }


class clv_person(osv.osv):
    _inherit = 'clv_person'

    _columns = {
        'community_ids': fields.one2many('clv_community.person',
                                         'person_id',
                                         'Community Roles'),
        # 'community_ids2': fields.one2many('clv_community.person',
        #                                   'person_id',
        #                                   'Communities'),
        }
