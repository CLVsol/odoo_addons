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

class clv_annotation(osv.osv):
    _name = 'clv_annotation'

    _columns = {
        'name': fields.char('Subject', size=64, select=1, required=True),
        'code': fields.char ('Annotation Code', size=128, required=False),
        'author': fields.many2one('res.users', 'Author', required=True, readonly=True),
        'date': fields.datetime("Date", required=True, readonly=True),
        'body': fields.text(string='Body'),
        'active': fields.boolean('Active', 
                                 help="If unchecked, it will allow you to hide the annotation without removing it."),
        }
     
    _sql_constraints = [
        ('uniq_annotation_code', 'unique(code)', "Error! The annotation code must be unique!"),
        ]

    _defaults = {
        'author': lambda obj,cr,uid,context: uid,
        'date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': 1,
        }
    
    _order = "date desc"

