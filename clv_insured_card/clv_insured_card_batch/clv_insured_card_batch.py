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

class clv_insured_card_batch(osv.Model):
    _name = 'clv_insured_card.batch'

    _columns = {
        'seq': fields.integer('Sequence', required=False),
        'batch_id': fields.many2one('clv_batch', 'Batch', required=False),
        'batch_category': fields.related('batch_id', 'name_category', type='char', string='Batch Category', 
                                         readonly=True, store=True),
        'insured_card_id': fields.many2one('clv_insured_card', string='Insured Card', help='Insured Card'),
        'sign_in_date': fields.datetime("Sign in date", required=False),
        'sign_out_date': fields.datetime("Sign out date", required=False),
        'notes': fields.text(string='Notes'),
        'active': fields.boolean('Active', 
                                 help="If unchecked, it will allow you to hide the insured card batch without removing it."),
    }

    # _order = "sign_in_date desc"
    _order = "seq"

    _defaults = {
        'sign_in_date': lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'active': 1,
    }

class clv_insured_card(osv.osv):
    _inherit = 'clv_insured_card'

    _columns = {
        'insured_card_batch_ids': fields.one2many('clv_insured_card.batch',
                                                  'insured_card_id',
                                                  'Insured Card Batches'),
    }

class clv_batch(osv.osv):
    _inherit = 'clv_batch'

    _columns = {
        'insured_card_batch_ids': fields.one2many('clv_insured_card.batch',
                                                  'batch_id',
                                                  'Insured Card Batches'),
    }
