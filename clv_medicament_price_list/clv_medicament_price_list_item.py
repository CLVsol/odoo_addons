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
# from datetime import datetime
# from dateutil.relativedelta import relativedelta

class clv_medicament_price_list_item(models.Model):
    _name = 'clv_medicament_price_list.item'

    price_list_id = fields.Many2one('clv_medicament_price_list', string='Medicament Price List',
                                     help='Medicament Price List', required=True)
    medicament_id = fields.Many2one('clv_medicament', string='Medicament',
                                     help='Medicament Name', required=True)
    notes = fields.Text(string='Notes')
    consumer_price = fields.Float('Consumer Price')
    production_price = fields.Float('Production Price')
    refund_price = fields.Float('Refund Price')

    _order='price_list_id, medicament_id'

class clv_medicament_price_list(models.Model):
    _inherit = 'clv_medicament_price_list'

    medicament_ids = fields.One2many('clv_medicament_price_list.item',
                                     'price_list_id',
                                     'Medicaments')
