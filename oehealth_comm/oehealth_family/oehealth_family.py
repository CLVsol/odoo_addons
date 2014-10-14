# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2012  Carlos Eduardo Vercelino - CLVsol                        #
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

from osv import osv
from osv import fields


class oehealth_family(osv.Model):
    _name = 'oehealth.family'

    _columns = {
        'community_area': fields.many2one('oehealth.comm_area', 
                                          string='Community Area',),
        'name': fields.char(size=256, 
                            string='Family', required=True, 
                            help='Family code within a community area'),
        'info': fields.text(string='Extra Information'),
        'members': fields.one2many('oehealth.family.member', 'family_id', 
                                   string='Family Members', ),
    }
    _sql_constraints = [('name_uniq', 'UNIQUE(name)', 'Family name must be unique!')]
