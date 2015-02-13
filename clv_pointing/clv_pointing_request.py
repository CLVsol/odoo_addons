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

from openerp import models, fields, api
from datetime import datetime

class clv_pointing_request(models.Model):
    _name = 'clv_pointing.request'
    
    name = fields.Many2one('clv_pointing.type','Pointing Type')
    date = fields.Datetime('Date',
                           default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    state = fields.Selection([('draft','Draft'),
                              ('executed','Executed'),
                              ('cancel','Cancel')
                              ], 'State',readonly=True)
    # request_id = fields.Many2one('clv_request','Batch')
    pointing_id = fields.Many2one('clv_pointing','Pointing')
    
    _defaults={
        'state' : lambda *a: 'draft',
        }
