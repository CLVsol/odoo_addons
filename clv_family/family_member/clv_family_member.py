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

class clv_family_member(models.Model):
    _name = 'clv_family.member'

    family_id = fields.Many2one('clv_family', string='Family',
                                help='Family', required=False)
    member_id = fields.Many2one('clv_person', string='Member')
    role = fields.Many2one('clv_family.member_role', 'Role', required=False)
    notes = fields.Text(string='Notes')
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the family member without removing it.",
                            default=1)

class clv_family(models.Model):
    _inherit = 'clv_family'

    member_ids = fields.One2many('clv_family.member',
                                 'family_id',
                                 'Members')

class clv_person(models.Model):
    _inherit = 'clv_person'

    family_member_ids = fields.One2many('clv_family.member',
                                        'member_id',
                                        'Family Members')
    # family_member_ids2 = fields.One2many('clv_family.member',
    #                                      'member_id',
    #                                      'Family Members')
