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
from dateutil.relativedelta import relativedelta

class clv_medicament_dispensation_ext(models.Model):
    _name='clv_medicament_dispensation_ext'

    name = fields.Char(size=32, string='Dispensation Code', required=False,
                       help='Type in the Code of this dispensation (ext)')
    authorization_code = fields.Char(size=32, string='Authorization Code', required=False)
    dispensation_date = fields.Date(string='Dispensation Date', required=False)
    insured_card_code = fields.Char(size=32, string='Insured Card Code', required=False)
    insured_name = fields.Char(size=256, string='Insured Name', required=False)
    prescriber_code = fields.Char(size=32, string='Prescriber Code', required=False)
    pharmacy_code = fields.Char(size=32, string='Pharmacy Code', required=False)
    pharmacy_name = fields.Char(size=256, string='Pharmacy Name', required=False)
    medicament_code = fields.Integer(string='Medicament Code')
    medicament_description = fields.Char(size=256, string='Medicament Description', required=False)
    notes = fields.Text(string='Dispensation Notes')
    # dispenser = fields.Many2one ('res.users', 'Dispenser')
    medicament_ref = fields.Reference([('clv_medicament', 'Medicament'),
                                       ], 'Medicament Reference')
    # medicament = fields.Many2one('clv_medicament', string='Dispensed Medicament', required=False, 
    #                               help='Dispensed Medicament')
    # max_retail_price = fields.Float('Maximum Retail Price')
    pack_quantity = fields.Integer(string='Pack Quantity',
                                   help='Quantity of packs of the medicament')
    # refund_price = fields.Float('Refund Price')
    # total_refund_price = fields.Float('Refund Value', size=32, compute='_total_refund_price', store=False)
    sale_value = fields.Float('Sale Value')
    subsidy_value = fields.Float('Subsidy Value')
    at_sight_value = fields.Float('At Sight Value')
    date_inclusion = fields.Datetime("Inclusion Date", required=False, readonly=False,
                                     default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the dispensation without removing it.",
                            default=1)
    
    _sql_constraints = [
        ('uniq_name', 'unique(name)', "Error! The Dispensation (Ext) Code must be unique!"),
        ]

    # _defaults={
    #     dispenser = lambda obj,cr,uid,context: uid, 
    #     }
