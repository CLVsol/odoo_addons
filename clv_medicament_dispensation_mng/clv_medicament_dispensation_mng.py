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

class clv_medicament_dispensation_mng(osv.Model):
    _name='clv_medicament_dispensation_mng'

    def _compute_total_refund_price(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        for r in self.browse(cr, uid, ids, context=context):
            result[r.id] = r.refund_price * r.pack_quantity
        return result

    _columns={
        'name': fields.char(size=256, string='Dispensation Code', required=False,
                            help='Type in the Code of this dispensation'),
        'dispensation_date': fields.date(string='Dispensation Date', required=False),
        'notes': fields.text(string='Dispensation Notes'),
        'dispenser' : fields.many2one ('res.users', 'Dispenser'),
        'medicament': fields.many2one('clv_medicament', string='Dispensed Medicament', required=False, 
                                      help='Dispensed Medicament'),
        'medicament_code': fields.related('medicament', 'code', type='char', string='Medicament Code', 
                                          readonly=True, store=False),
        'max_retail_price': fields.float('Maximum Retail Price'),
        'pack_quantity': fields.integer(string='Pack Quantity',
                                        help='Quantity of packs of the medicament'),
        'refund_price': fields.float('Refund Price'),
        'total_refund_price' : fields.function(_compute_total_refund_price, method=True, type='float', size=32, 
                                               string='Refund Value',),
        'active': fields.boolean('Active', help="The active field allows you to hide the dispensation without removing it."),

        'cod_prod': fields.integer(string='Cod Prod'),
        'orizon_id': fields.many2one('clv_orizon', string='Orizon'),
        'crd_code': fields.char(size=32, string='Insured Card Code', required=False),
        'crm': fields.char(size=32, string='CRM', required=False),
        'pharmacy_cnpj': fields.char(size=32, string='CNPJ', required=False),
        'sale_value': fields.float('Sale Value'),
        'at_sight_value': fields.float('At Sight Value'),
        'dispensation_id': fields.many2one('clv_medicament_dispensation',
                                           string='Dispensation', ),
        }
    
    _sql_constraints = [
        ('uniq_name', 'unique(name)', "Error! The Dispensation Code must be unique!"),
        ]

    _defaults={
        # 'dispensation_date': lambda *a: datetime.now().strftime('%Y-%m-%d'),
        'active': 1,
        # 'dispenser': lambda obj,cr,uid,context: uid, 
        }
