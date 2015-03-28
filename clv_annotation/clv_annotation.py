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
from openerp.osv import osv
from datetime import *

class clv_annotation(models.Model):
    _name = 'clv_annotation'

    name = fields.Char('Subject', size=64, select=1, required=True)
    code = fields.Char ('Code',size=128, required=False)
    author = fields.Many2one('res.users', 'Author', required=True, readonly=True,
                             default=lambda self: self._uid)
    date = fields.Datetime("Date", required=True, readonly=True,
                           default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    body = fields.Text(string='Body')
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the annotation without removing it.",
                            default=1)
    
    _sql_constraints = [
        ('uniq_annotation_code', 'unique(code)', "Error! The annotation code must be unique!"),
        ]

    _order = "date desc"

