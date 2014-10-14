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
        'medirecon_medication_template_ids': fields.one2many('oehealth.medirecon.medication.template',
                                                             'inpatient_reg',
                                                             'Medication Templates'),
        }

class oehealth_medirecon_medication_template(osv.Model):
    _name = 'oehealth.medirecon.medication.template'

    _columns = {
        'name': fields.char(size=256, string='Name'),
        'patient' : fields.many2one ('oehealth.patient','Patient'),
        'inpatient_reg' : fields.many2one ('oehealth.hospital.inpatient_registration','Inpatient Registration'),
        'researcher' : fields.many2one ('oehealth.researcher','Researcher'),
        'date': fields.date("Date"),
        'info_source': fields.selection([
                                         ('(a) Paciente', 'Paciente'),
                                         ('(b) Cuidador', 'Cuidador'),
                                         ('(c) Prontuario', 'Prontuario'),
                                         ('(d) Equipe multiprofissional', 'Equipe multiprofissional'),
                                         ('(e) Receita Medica', 'Receita Medica'),
                                         ], string='Fonte de informacao',
                                         help=''),
        'medicament': fields.many2one('oehealth.medicament',
                                      string='Medicament',required=True, 
                                      help='Prescribed Medicament'),
        'dose': fields.float(string='Dose', 
                             help='Amount of medication (eg, 250 mg) per dose'),
                
        'dose_unit': fields.many2one('product.uom',
                                     string='dose unit', 
                                     help='Unit of measure for the medication to be taken'),
        'frequency': fields.integer(string='Frequency', 
                                     help='Time in between doses the patient must wait (ie, for 1 pill'\
                                     ' each 8 hours, put here 8 and select \"hours\" in the unit field'),
        'frequency_unit': fields.selection([
                                            ('seconds', 'seconds'),
                                            ('minutes', 'minutes'),
                                            ('hours', 'hours'),
                                            ('days', 'days'),
                                            ('weeks', 'weeks'),
                                            ('months', 'months'),
                                            ('wr', 'when required'),
                                            ], string='unit',select=True, sort=False),
        'frequency_prn': fields.boolean(string='PRN', help='Use it as needed, pro re nata'),
        #'indication': fields.many2one('oehealth.pathology',
        #                              string='Indication', 
        #                              help='Choose a disease for this medicament from the disease list. It'\
        #                              ' can be an existing disease of the patient or a prophylactic.'),
        'indication': fields.char(size=256, string='Indication'),
        #'start_treatment': fields.datetime(string='Start', help='Date of start of Treatment'),
        'start': fields.char(size=256, string='Inicio'),
        'last_dose': fields.char(size=256, string='Ultima dose'),
        'prescribed_at_admission': fields.selection([
                                                     ('S', 'Sim'),
                                                     ('N', 'Nao'),
                                                     ], string='Prescrito na admissao?',select=True, sort=False),
        'prescribed_at_discharge': fields.selection([
                                                     ('S', 'Sim'),
                                                     ('N', 'Nao'),
                                                     ], string='Prescrito na alta?',select=True, sort=False),
        'problem': fields.selection([
                                     ('(A) Medicamento nao prescrito', 'Medicamento nao prescrito'),
                                     ('(B) Medicamento prescrito em subdose', 'Medicamento prescrito em subdose'),
                                     ('(C) Medicamento prescrito em sobredose', 'Medicamento prescrito em sobredose'),
                                     ('(D) Medicamento prescrito que paciente ja teve RAM', 'Medicamento prescrito que paciente ja teve RAM'),
                                     ('(E) Medicamento substituido por mesma classe', 'Medicamento substituido por mesma classe'),
                                     ('(F) Interacao medicamentosa', 'Interacao medicamentosa'),
                                     ], string='Problema identificado na admissao',select=True, sort=False),
        'problem2': fields.selection([
                                      ('(A) Medicamento nao prescrito', 'Medicamento nao prescrito'),
                                      ('(B) Medicamento prescrito em subdose', 'Medicamento prescrito em subdose'),
                                      ('(C) Medicamento prescrito em sobredose', 'Medicamento prescrito em sobredose'),
                                      ('(D) Medicamento prescrito que paciente ja teve RAM', 'Medicamento prescrito que paciente ja teve RAM'),
                                      ('(E) Medicamento substituido por mesma classe', 'Medicamento substituido por mesma classe'),
                                      ('(F) Interacao medicamentosa', 'Interacao medicamentosa'),
                                      ], string='Problema identificado na alta',select=True, sort=False),
        'intetional': fields.selection([
                                        ('(1) Nao intecional', 'Nao intecional'),
                                        ('(2) Intencional', 'Intencional'),
                                        ], string='Intencionalidade na admissao',select=True, sort=False),
        'intetional2': fields.selection([
                                         ('(1) Nao intecional', 'Nao intecional'),
                                         ('(2) Intencional', 'Intencional'),
                                         ], string='Intencionalidade na alta',select=True, sort=False),
        'intervention': fields.text(string='Intervenção na admissão',
                                    help='Intervenção na admissão'),
        'intervention2': fields.text(string='Intervenção na alta',
                                     help='Intervenção na alta'),

        
        #'form': fields.many2one('oehealth.drug.form', string='Form', 
        #                         help='Drug form, such as tablet or gel'),
        #'route': fields.many2one('oehealth.drug.route',
        #                         string='Administration Route', 
        #                         help='Drug administration route code.'),
        #'duration_period': fields.selection([
        #                                     ('minutes', 'minutes'),
        #                                     ('hours', 'hours'),
        #                                     ('days', 'days'),
        #                                     ('months', 'months'),
        #                                     ('years', 'years'),
        #                                     ('indefinite', 'indefinite'),
        #                                     ], string='Treatment period',
        #                                    help='Period that the patient must take the medication in minutes,'\
        #                                    ' hours, days, months, years or indefinately'),
        #'qty': fields.integer(string='x',
        #                      help='Quantity of units (eg, 2 capsules) of the medicament'),
        #'duration': fields.integer(string='Treatment duration',
        #                           help='Period that the patient must take the medication. in minutes,'\
        #                           ' hours, days, months, years or indefinately'),
        #'common_dosage': fields.many2one('oehealth.medication.dosage',
        #                                 string='Frequency', 
        #                                 help='Common / standard dosage frequency for this medicament'),
        #'admin_times': fields.char(size=256, string='Admin hours', 
        #                           help='Suggested administration hours. For example, at 08:00, 13:00'\
        #                           ' and 18:00 can be encoded like 08 13 18'),
        #'end_treatment': fields.datetime(string='End', help='Date of end of Treatment'),
        }
