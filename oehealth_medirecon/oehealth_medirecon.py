# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2012  Carlos Eduardo Vercelino - CLVsol                        #
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

from osv import osv
from osv import fields


class oehealth_hospital_inpatient_registration (osv.osv):
    _name = "oehealth.hospital.inpatient_registration"
    _inherit = "oehealth.hospital.inpatient_registration"

    _columns = {
        'adhesion': fields.selection([
                                     ('S', 'Sim'),
                                     ('N', 'Nao'),
                                     ], string='O paciente assinou o TCLE?',
                                     select=True, sort=False),
        'medicament_allergic': fields.selection([
                                                ('Sim', 'Sim'),
                                                ('Nao', 'Nao'),
                                                ('Nao sabe', 'Nao Sabe')
                                                ], string='O paciente é alérgico a algum medicamento?',
                                                select=True, sort=False),
        'medicaments': fields.text(string='Quais Medicamentos',
                                    help='Lista de medicamentos aos quais o paciente é alergico'),
        'medicament_provider': fields.selection([
                                                ('Posto de Saude', 'Posto de Saude'),
                                                ('Farmacia', 'Farmacia'),
                                                ('HC', 'HC'),
                                                ('Farmacia Popular', 'Farmacia Popular'),
                                                ('HC e Posto', 'HC e Posto'),
                                                ('HC e Farmacia', 'HC e Farmacia'),
                                                ('Posto e Farmacia', 'Posto e Farmacia'),
                                                ('Nao sabe', 'Nao Sabe')
                                                ], string='Onde o paciente retira os medicamentos?',
                                                select=True, sort=False),
        'doctor': fields.selection([
                                   ('S', 'Sim'),
                                   ('N', 'Nao'),
                                   ], string='O paciente tem acompanhamento medico?',
                                   select=True, sort=False),
        }

