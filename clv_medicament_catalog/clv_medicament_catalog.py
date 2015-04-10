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

class clv_medicament_catalog(osv.osv):
    _name = 'clv_medicament_catalog'
    
    _columns = {
        'name': fields.char('Medicament Catalog Name', required=True, size=64, translate=True),
        'alias' : fields.char('Alias', size=64, help='Common name that the Medicament Catalog is referred'),
        'code': fields.char(size=64, string='Medicament Catalog Code', required=False),
        'notes':  fields.text(string='Notes'),
        'date_inclusion': fields.datetime("Inclusion Date", required=False, readonly=False),
        'active': fields.boolean('Active', 
                                 help="The active field allows you to hide the medicament catalog without removing it."),
    }

    _sql_constraints = [('code_uniq', 'unique(code)', u'Duplicated Catalog Code!')]
    
    _defaults = {
        'date_inclusion': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': 1,
    }
    
    _order = 'name'
