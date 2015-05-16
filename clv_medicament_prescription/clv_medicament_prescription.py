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
from dateutil.relativedelta import relativedelta

class clv_medicament_prescription(osv.Model):
    _name='clv_medicament_prescription'

    def _age(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        now = datetime.now()
        for r in self.browse(cr, uid, ids, context=context):
            if r.prescription_date:
                dob = datetime.strptime(r.prescription_date,'%Y-%m-%d')
                delta=relativedelta (now, dob)
                result[r.id] = str(delta.years) +"y "+ str(delta.months) +"m "+ str(delta.days)+"d"
            else:
                result[r.id] = "No Date of Birth!"
        return result

    _columns={
        'name': fields.char(size=256, string='Prescription Code', required=True,
                            help='Type in the Code of this prescription'),
        'prescription_date': fields.date(string='Prescription Date', required=False),
        'age': fields.function(_age, type="char", string='Age', store=False),
        'notes': fields.text(string='Prescription Notes'),
        'active': fields.boolean('Active', help="The active field allows you to hide the prescription without removing it."),
        'transcription_date': fields.date(string='Transcription Date', required=False),
        'transcriber' : fields.many2one ('res.users', 'Transcriber'),
        }
    
    _sql_constraints = [
        ('uniq_name', 'unique(name)', "Error! The Prescription Code must be unique!"),
        ]

    _defaults={
        'prescription_date': lambda *a: datetime.now().strftime('%Y-%m-%d'),
        'active': 1,
        'transcription_date': lambda *a: datetime.now().strftime('%Y-%m-%d'),
        'transcriber': lambda obj,cr,uid,context: uid, 
        }
