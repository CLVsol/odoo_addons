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

class clv_medicament_dispensation(osv.Model):
    _name='clv_medicament.dispensation'

    _columns={
        'name': fields.char(size=256, string='Dispensation Code', required=True,
                            help='Type in the Code of this dispensation'),
        'dispensation_date': fields.date(string='Dispensation Date', required=False),
        'notes': fields.text(string='Dispensation Notes'),
        'active': fields.boolean('Active', help="The active field allows you to hide the dispensation without removing it."),
        }
    
    _sql_constraints = [
                        ('uniq_name', 'unique(name)', "The Dispensation Code must be unique!"),
                        ]

    _defaults={
        'dispensation_date': lambda *a: datetime.now().strftime('%Y-%m-%d'),
        'active': 1,
        }
