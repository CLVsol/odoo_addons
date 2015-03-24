# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).                        #
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

class clv_insured_mng(models.Model):
    _inherit = 'clv_insured_mng'

    insured_card_id = fields.Many2one('clv_insured_card', 'Insured Card', ondelete='restrict')
    crd_name = fields.Char('Printed Name', required=False, size=64, help='Name printed on the card.')
    crd_code = fields.Char(size=64, string='Insured Card Code')
    crd_notes = fields.Text(string='Notes')
