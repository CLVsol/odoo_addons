# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2012  Carlos Eduardo Vercelino - CLVsol.net                    #
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
import time

class oehealth_patient_data (osv.osv):
    _name = "oehealth.patient"
    _inherit = "oehealth.patient"

#    def name_get(self, cr, uid, ids, context={}):
#        if not len(ids):
#            return []
#        rec_name = 'name'
#        res = [(r['id'], r[rec_name][1]) for r in self.read(cr, uid, ids, [rec_name], context)]
#        return res

    def name_search(self, cr, user, name='', args=None, operator='ilike', context=None, limit=80):
        if not args:
            args=[]
        if not context:
            context={}
        if name:
            ids = self.search(cr, user, [('patient_id','=',name)]+ args, limit=limit, context=context)
            if not len(ids):
                ids += self.search(cr, user, [('name',operator,name)]+ args, limit=limit, context=context)
        else:
            ids = self.search(cr, user, args, limit=limit, context=context)
        result = self.name_get(cr, user, ids, context)
        return result        

    _columns = {
        'lab_test_ids': fields.one2many('oehealth.patient.lab_test','patient_id','Lab Tests Required'),
        }

class lab_test_type (osv.osv):
    _name = "oehealth.lab_test.type"
    _description = "Type of Lab test"
    _columns = {
        'name' : fields.char ('Test',size=128,help="Test type, eg X-Ray, hemogram, biopsy..."),
        'code' : fields.char ('Code',size=32,help="Short name - code for the test"),
        'info' : fields.text ('Description'),
        #'product_id' : fields.many2one('product.product', 'Service', required=True),
        'critearea': fields.one2many('oehealth.lab_test.critearea','lab_test_type_id','Test Cases'),
    }
    _sql_constraints = [
                        ('name_uniq', 'unique (name)', 'The Lab Test name must be unique'),
                        ('code_uniq', 'unique (code)', 'The Lab Test code must be unique')
                        ]

class oehealth_lab_test (osv.osv):
    _name = "oehealth.lab_test"
    _description = "Lab Test"
    _columns = {
        'name' : fields.char ('ID', size=128, help="Lab Teste result ID"),
        'test' : fields.many2one ('oehealth.lab_test.type', 'Lab Test type', help="Lab test type"),
        'patient' : fields.many2one ('oehealth.patient', 'Patient', help="Patient ID"), 
        'pathologist' : fields.many2one ('oehealth.physician','Pathologist',help="Pathologist"),
        'requestor' : fields.many2one ('oehealth.physician', 'Doctor', help="Doctor who requested the test"),
        'results' : fields.text ('Results'),
        'diagnosis' : fields.text ('Diagnosis'),
        'critearea': fields.one2many('oehealth.lab_test.critearea','lab_test_id','Test Cases'),
        'date_requested' : fields.datetime ('Date requested'),
        'date_analysis' : fields.datetime ('Date of the Analysis'),        
        }

    _defaults = {
        'date_requested': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        'date_analysis': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        'name' : lambda obj, cr, uid, context: obj.pool.get('ir.sequence').get(cr, uid, 'oehealth.lab_test'),         
         }

    _sql_constraints = [('id_uniq', 'unique (name)', 'The test ID code must be unique')]
    
class oehealth_lab_test_units(osv.osv):
    _name = "oehealth.lab_test.units"
    _columns = {
        'name' : fields.char('Unit', size=25),
        'code' : fields.char('Code', size=25),
        }
    _sql_constraints = [
                        ('name_uniq', 'unique(name)', 'The Unit name must be unique'),
                        ('code_uniq', 'unique(code)', 'The Unit code must be unique')
                        ]
    
class oehealth_lab_test_critearea(osv.osv):
    _name = "oehealth.lab_test.critearea"
    _description = "Lab Test Critearea"    
    _columns ={
       'name' : fields.char('Test', size=64),
       'result' : fields.text('Result'),
       'normal_range' : fields.text('Normal Range'),
       'units' : fields.many2one('oehealth.lab_test.units', 'Units'),
       'lab_test_type_id' : fields.many2one('oehealth.lab_test.type','Test type'),
       'lab_test_id' : fields.many2one('oehealth.lab_test','Test Cases'),
       'sequence' : fields.integer('Sequence'),       
       }
    _defaults = {
         'sequence' : lambda *a : 1,        
         }
    _order="sequence"

class oehealth_patient_lab_test(osv.osv):
    _name = 'oehealth.patient.lab_test'
    
    #def _get_default_dr(self, cr, uid, context={}):
    #    partner_id = self.pool.get('res.partner').search(cr,uid,[('user_id','=',uid)])
    #    if partner_id:
    #        dr_id = self.pool.get('hr.employee').search(cr,uid,[('name','=',partner_id[0])])
    #        if dr_id:
    #            return dr_id[0]
            #else:
            #    raise osv.except_osv(_('Error !'),
            #            _('There is no physician defined ' \
            #                    'for current user.'))
     #   else:
     #       return False
        
    _columns = {
        'name' : fields.many2one('oehealth.lab_test.type','Lab Test Type'),
        'date' : fields.datetime('Date'),
        'state' : fields.selection([('draft','Draft'),('tested','Tested'),('cancel','Cancel')],'State',readonly=True),
        'patient_id' : fields.many2one('oehealth.patient','Patient'),
        'doctor_id' : fields.many2one('oehealth.physician','Doctor', help="Doctor who Request the lab test."), 
        #'invoice_status' : fields.selection([('invoiced','Invoiced'),('tobe','To be Invoiced'),('no','No Invoice')],'Invoice Status'),
        #'lab_test_id': fields.one2many('oehealth.lab_test','patient_lab_test_id','Patient Lab Test'),
        'lab_test_id': fields.many2one('oehealth.lab_test','name','Patient Lab Test'),
        }
    
    _defaults={
       'date' : lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
       'state' : lambda *a : 'draft',
       #'doctor_id' : _get_default_dr,        
       #'invoice_status': lambda *a: 'tobe',
       }

