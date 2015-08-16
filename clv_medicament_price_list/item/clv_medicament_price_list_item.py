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

    price_list_version_id = fields.Many2one('clv_medicament_price_list.version', string='Medicament Price List Version',
                                            help='Medicament Price List Version', required=True)
    # medicament_id = fields.Many2one('clv_medicament', string='Medicament',
    #                                  help='Medicament Name', required=True)
    # medicament_id = fields.Reference([('clv_medicament', 'Medicament'),
    #                                   ('clv_orizon_lpm', 'Medicament (Orizon LPM)'),
    #                                   ])
    medicament_id2 = fields.Reference([('clv_orizon_lpm', 'Medicament (Orizon LPM)'),
                                       ('clv_medicament', 'Medicament'),
                                       ])
    notes = fields.Text(string='Notes')
    consumer_price = fields.Float('Consumer Price')
    production_price = fields.Float('Production Price')
    refund_price = fields.Float('Refund Price')

    _order='price_list_version_id, medicament_id2'

class clv_medicament_price_list_version(models.Model):
    _inherit = 'clv_medicament_price_list.version'

    medicament_ids = fields.One2many('clv_medicament_price_list.item',
                                     'price_list_version_id',
                                     'Medicaments')
