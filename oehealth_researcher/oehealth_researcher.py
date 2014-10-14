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


class oehealth_researcher(osv.Model):
    _name = 'oehealth.researcher'

    _columns = {
        'name': fields.char(size=256, string='Name', required=True),
        'info': fields.text(string='Extra info'),
        'code': fields.char(size=256, string='ID'),
        'health_professional': fields.many2one('res.partner',
                                               string='Health Professional',
                                               help='Health Professional\'s Name, from the partner list' ),
        'institution': fields.many2one('res.partner', string='Institution',
                                        help='Instituion where she/he works' ),
    }
