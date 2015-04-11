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

class clv_medicament_group(osv.osv):
    _name = 'clv_medicament_group'

    _columns = {
        'name' : fields.char('Name', size=64, select=1, required=True, help='Medicament Group Name'),
        'alias' : fields.char('Alias', size=64, help='Common name that the Medicament Group is referred'),
        'code': fields.char(size=64, string='Medicament Group Code', required=False),
        'notes':  fields.text(string='Notes'),
        'date_inclusion': fields.datetime("Inclusion Date", required=False, readonly=False),
        'catalog_id': fields.many2one('clv_medicament_catalog', 'Catalog'),
        'active': fields.boolean('Active', 
                                 help="The active field allows you to hide the group without removing it."),
        'medicament_name': fields.char(size=256, string='Medicament Name'),
        'active_component': fields.many2one('clv_medicament.active_component', 
                                            string='Active Component', 
                                            help='Medicament Active Component'),
        'concentration': fields.char(size=256, string='Concentration'),
        'pres_form': fields.char(size=256, string='Presentation Form'),
        'catalog_name': fields.related('catalog_id', 'name', type='char', string='Catalog Name', 
                                       readonly=True, store=True),
        }

    _order='catalog_name, name'

    _defaults = {
        'date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': True,
        }
