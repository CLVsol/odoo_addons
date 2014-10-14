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

from osv import fields, osv

class oehealth_patient_data (osv.osv):
    _name = "oehealth.patient"
    _inherit = "oehealth.patient"

    _columns = {
        'inpatient_registration_ids': fields.one2many('oehealth.hospital.inpatient_registration','patient','Inpatient Registrations'),
        }

class oehealth_hospital_inpatient_registration (osv.osv):
    
    # Method to check for availability and make the hospital bed reservation

    #def registration_confirm(self, cr, uid, ids, context={}):
    #    for reservation in self.browse(cr,uid,ids):
    #        bed_id= str(reservation.bed.id)
    #        cr.execute("select count (*) from medical_inpatient_registration where (hospitalization_date::timestamp,discharge_date::timestamp) overlaps ( timestamp %s , timestamp %s ) and state= %s and bed = cast(%s as integer)", (reservation.hospitalization_date,reservation.discharge_date,'confirmed',bed_id))
    #        res = cr.fetchone()
    #
    #    if res[0] > 0:
    #        raise osv.except_osv('Warning', 'Bed has been already reserved in this period' ) 
    #    else:
    #        self.write(cr, uid, ids, {'state':'confirmed'})
    #    return True

    #def patient_discharge(self, cr, uid, ids, context={}):
    #    self.write(cr, uid, ids, {'state':'free'})
    #    return True

    #def registration_cancel(self, cr, uid, ids, context={}):
    #    self.write(cr, uid, ids, {'state':'cancelled'})
    #    return True

    #def registration_admission(self, cr, uid, ids, context={}):
    #    self.write(cr, uid, ids, {'state':'hospitalized'})
    #    return True

    _name = "oehealth.hospital.inpatient_registration"
    _description = "Patient admission History"
    _columns = {
        'name' : fields.char ('Registration Code',size=128),
        'patient' : fields.many2one ('oehealth.patient','Patient'),
        'admission_type' : fields.selection([('routine','Routine'),
                                             ('maternity','Maternity'),
                                             ('elective','Elective'),
                                             ('urgent','Urgent'),
                                             ('emergency','Emergency')],'Admission type'),
        'admission_area' : fields.selection([('c','Clínica Cirúrgica'),
                                             ('m','Clínica Médica')],'Admission area'),
        'hospitalization_date' : fields.datetime ('Hospitalization date'),
        'discharge_date' : fields.datetime ('Discharge date'),
        #'attending_physician' : fields.many2one ('oehealth.physician','Attending Physician'),
        #'operating_physician' : fields.many2one ('oehealth.physician','Operating Physician'),
        #'admission_reason' : fields.many2one ('oehealth.pathology','Reason for Admission', help="Reason for Admission"),
        'admission_reason' : fields.char ('Reason for Admission',size=256),
        #'bed' : fields.many2one ('medical.hospital.bed','Hospital Bed'),
        #'nursing_plan' : fields.text ('Nursing Plan'),
        #'discharge_plan' : fields.text ('Discharge Plan'),

        'info' : fields.text ('Extra Info'),
        'state': fields.selection((('free','free'),
                                   ('cancelled','cancelled'),
                                   ('confirmed','confirmed'),
                                   ('hospitalized','hospitalized')),'Status'),
        }

    _defaults = {
        #'name': lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'oehealth.hospital.inpatient_registration'),
        #'state': lambda *a : 'free'
    }

    sql_constraints = [('name_uniq', 'unique (name)', 'The Registration code already exists')]
