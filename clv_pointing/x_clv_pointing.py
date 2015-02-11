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

class clv_pointing (models.Model):
    _name = "clv_pointing"

    name = fields.Char('ID', size=128, help="Pointing result ID")
    pointing_type = fields.Many2one('clv_pointing.type', 'Pointing type', help="Pointing type")
    batch = fields.Many2one('clv_batch', 'Batch', help="Batch ID")
    results = fields.Text('Results')
    diagnosis = fields.Text('Diagnosis')
    criteria = fields.One2many('clv_pointing.criterion','pointing_id','Pointing Cases')
    date_requested = fields.Datetime('Date requested',
                                      default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    date_execution = fields.Datetime('Date of the Execution')       

    _sql_constraints = [('id_uniq', 'unique (name)', 'Error! The pointing ID must be unique!')]
    
