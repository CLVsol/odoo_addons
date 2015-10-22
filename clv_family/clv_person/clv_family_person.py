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

class clv_family_person(models.Model):
    _name = 'clv_family.person'

    family_id = fields.Many2one('clv_family', string='Family',
                                help='Family', required=False)
    person_id = fields.Many2one('clv_person', string='Person')
    role = fields.Many2one('clv_family.person_role', 'Role', required=False)
    notes = fields.Text(string='Notes')
    active = fields.Boolean('Active', 
                            help="If unchecked, it will allow you to hide the person without removing it.",
                            default=1)

class clv_family(models.Model):
    _inherit = 'clv_family'

    person_ids = fields.One2many('clv_family.person',
                                 'family_id',
                                 'Persons')

class clv_person(models.Model):
    _inherit = 'clv_person'

    family_ids = fields.One2many('clv_family.person',
                                 'person_id',
                                 'Families')
    family_ids2 = fields.One2many('clv_family.person',
                                  'person_id',
                                  'Families')
