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

class clv_tag(osv.osv):
    _inherit = 'clv_tag'

    _columns = {
        'state': fields.selection([('draft','Draft'),
                                   ('revised','Revised'),
                                   ('done','Done')
                                   ], string='Status', readonly=True, required=True, help="")
        }
    
    _defaults = {
        'state': 'draft',
        }

    def button_draft(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'draft'})

    def button_revised(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'revised'})

    def button_done(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'done'})
