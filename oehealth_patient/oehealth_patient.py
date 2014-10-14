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
from openerp import tools

class oehealth_patient(osv.Model):
    _name='oehealth.patient'
    _inherits={
               'oehealth.person': 'person_id',
               }
    
    _columns={
        'patient_code': fields.char(size=64, string='Patient Code'),
        'person_id': fields.many2one('oehealth.person', 'Related Person', required=True,
                                     ondelete='cascade', help='Person-related data of the patient'),
        #we need a related field in order to be able to sort the person by name
        'name_related': fields.related('person_id', 'name', type='char', string='Related Person', 
                                       readonly=True, store=True),
        'blood_type': fields.selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'),
                                        ('O', 'O'), ], string='Blood Type'),
        'rh': fields.selection([('+', '+'), ('-', '-'), ], string='Rh'),
        'general_info': fields.text(string='General Information',
                                    help='General information about the patient'),
        #'primary_care_doctor': fields.many2one('oehealth.physician',
        #                                       'Primary Care Doctor', 
        #                                       help='Current primary care / family doctor'),
        'childbearing_age': fields.boolean('Potential for Childbearing'),
        #'medications': fields.one2many('oehealth.patient.medication',
        #                               'patient_id', string='Medications',),
        #'evaluations': fields.one2many('oemedical.patient.evaluation',
        #                               'patient_id', string='Evaluations',),
        'critical_info': fields.text(string='Important disease, allergy or procedures information',
                                     help='Write any important information on the patient\'s disease,'\
                                     ' surgeries, allergies, ...'),
        #'current_address': fields.many2one('res.partner', string='Address',
        #                                   help='Contact information. You may choose from the different contacts'\
        #                                   ' and addresses this patient has.'),
        #'diseases': fields.one2many('oemedical.patient.disease',
        #                            'patient_id', string='Diseases',
        #                            help='Mark if the patient has died'),
        #'ethnic_group': fields.many2one('oemedical.ethnicity',
        #                                string='Ethnic group',),
        #'ssn': fields.char(size=256, string='SSN',),
        #'vaccinations': fields.one2many('oemedical.vaccination', 'patient_id',
        #                                'Vaccinations',),
        'dod': fields.datetime(string='Date of Death'),
        #'current_insurance': fields.many2one('oemedical.insurance',
        #                                     string='Insurance',
        #        help='Insurance information. You may choose from the different'\
        #' insurances belonging to the patient'),
        #'cod': fields.many2one('oemedical.pathology',
        #                       string='Cause of Death',),
        #'identification_code': fields.char(size=256, string='ID',
        #    help='Patient Identifier provided by the Health Center.Is not the'\
        #    ' Social Security Number'),
        'deceased': fields.boolean(string='Deceased'),
   }
    
    _order='name_related'

    _defaults={
               'is_person': 1,
               }

    _sql_constraints = [
                        ('patient_code_uniq', 'unique(patient_code)', 'Patient code already in use!'),
                        ]
