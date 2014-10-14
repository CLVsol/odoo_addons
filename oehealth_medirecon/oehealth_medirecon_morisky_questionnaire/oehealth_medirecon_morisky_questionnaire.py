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
        'medirecon_morisky_questionnaire_ids': fields.one2many('oehealth.medirecon.morisky.questionnaire',
                                                               'inpatient_reg',
                                                               'Morisky Questionnairies'),
        }

class oehealth_medirecon_morisky_questionnaire(osv.Model):
    _name = 'oehealth.medirecon.morisky.questionnaire'

    _columns = {
        'patient' : fields.many2one ('oehealth.patient','Patient'),
        'inpatient_reg' : fields.many2one ('oehealth.hospital.inpatient_registration','Inpatient Registration'),
        'researcher' : fields.many2one ('oehealth.researcher','Researcher'),
        'date': fields.date("Date"),
        'question01': fields.selection([
                                       ('S', 'Sim'),
                                       ('N', 'Nao'),
                                       ], string='Você, alguma vez, se esquece de tomar o seu remédio?',
                                       select=True, sort=False),
        'question02': fields.selection([
                                       ('S', 'Sim'),
                                       ('N', 'Nao'),
                                       ], string='Você, às vezes, é descuidado quanto ao horário de tomar o seu remédio?',
                                       select=True, sort=False),
        'question03': fields.selection([
                                       ('S', 'Sim'),
                                       ('N', 'Nao'),
                                       ], string='Quando você se sente bem, alguma vez, deixa de tomar seu remédio?',
                                       select=True, sort=False),
        'question04': fields.selection([
                                       ('S', 'Sim'),
                                       ('N', 'Nao'),
                                       ], string='Quando você se sente mal, com o remédio, às vezes, deixa de tomá-lo?',
                                       select=True, sort=False),
        'adherence': fields.integer('Adherence'),
        }
