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
from datetime import datetime

class clv_medicament_catalog_member(osv.Model):
    _name = 'clv_medicament_catalog_member'

    _columns = {
        'catalog_id': fields.many2one('clv_medicament_catalog', string='Medicament Catalog',
                                    help='Medicament Catalog', required=True),
        'medicament_id': fields.many2one('clv_medicament', string='Medicament',
                                         help='Medicament Name', required=False),
        'notes':  fields.text(string='Notes'),
        'level': fields.integer(string='Level'),
        'order': fields.integer(string='Order'),
        'date_inclusion': fields.datetime("Inclusion Date", required=False, readonly=False),
        'active': fields.boolean('Active', 
                                 help="The active field allows you to hide the catalog member without removing it."),
    }
    
    _order='level'
    
    _defaults = {
        'level': 1,
        'order': 10,
        'date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': True,
        }
