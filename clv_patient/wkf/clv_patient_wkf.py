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

class clv_patient(osv.osv):
    _inherit = 'clv_patient'

    _columns = {
        'date': fields.datetime("Status change date", required=True, readonly=True),
        'date_activation': fields.datetime("Activation date", required=False, readonly=False),
        'date_inactivation': fields.datetime("Inactivation date", required=False, readonly=False),
        'date_suspension': fields.datetime("Suspension date", required=False, readonly=False),
        'state': fields.selection([('new','New'),
                                   ('active','Active'),
                                   ('inactive','Inactive'),
                                   ('suspended','Suspended')
                                   ], string='Status', readonly=True, required=True, help=""),
        }
    
    _defaults = {
        'date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'state': 'new',
        }

    def button_new(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                  'state': 'new'})

    def button_activate(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  'date_activation':  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  'state': 'active'})

    def button_inactivate(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                  'date_inactivation':  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  'state': 'inactive'})

    def button_suspend(self, cr, uid, ids):
        self.write(cr, uid, ids, {'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                                  'date_suspension':  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                  'state': 'suspended'})
