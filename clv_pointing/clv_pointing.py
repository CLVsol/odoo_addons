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

class clv_pointing(osv.osv):
    _name = 'clv_pointing'

    _columns = {
        # 'name': fields.char('Name', required=True, size=64),
        'name': fields.char('Name', required=False, size=128),
        'alias': fields.char('Alias', size=64, help='Common name that the Pointing is referred'),
        'code': fields.char(size=64, string='Pointing Code', required=False),
        'notes': fields.text(string='Notes'),
        'date': fields.datetime("Date", required=False, readonly=False),
        'active': fields.boolean('Active', 
                                 help="If unchecked, it will allow you to hide the pointing without removing it."),
        'responsible': fields.many2one('res.users', 'Responsible', required=False, readonly=False),

        # name = fields.Char ('ID', size=128, help="Pointing result ID")
        'pointing_type': fields.many2one ('clv_pointing.type', 'Pointing type', help="Pointing type"),
        'batch': fields.many2one('clv_batch', 'Batch', help="Batch"),
        # results = fields.Text ('Results')
        # diagnosis = fields.Text ('Diagnosis')
        'criteria': fields.one2many('clv_pointing.criterion','pointing_id','Pointing Cases'),
        'date_requested': fields.datetime ('Date requested',
                                          default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        'date_execution': fields.datetime ('Date of the Execution'),      
        }

    _defaults = {
        'date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': 1,
        # 'responsible': lambda obj,cr,uid,context: uid,
        }
    
    _sql_constraints = [('pointing_code_uniq', 'unique(code)', u'Error! The Pointing Code must be unique!')]

    _order='name'
