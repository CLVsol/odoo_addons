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

def format_code(code_seq):
    code = map(int, str(code_seq))
    code_len = len(code)
    while len(code) < 14:
        code.insert(0, 0)
    while len(code) < 16:
        n = sum([(len(code) + 1 - i) * v for i, v in enumerate(code)]) % 11
        if n > 1:
            f = 11 - n
        else:
            f = 0
        code.append(f)
    code_str = "%s.%s.%s.%s.%s-%s" % (str(code[0]) + str(code[1]),
                                      str(code[2]) + str(code[3]) + str(code[4]),
                                      str(code[5]) + str(code[6]) + str(code[7]),
                                      str(code[8]) + str(code[9]) + str(code[10]),
                                      str(code[11]) + str(code[12]) + str(code[13]),
                                      str(code[14]) + str(code[15]))
    if code_len <= 3:
        code_form = code_str[18 - code_len:21]
    elif code_len > 3 and code_len <= 6:
        code_form = code_str[17 - code_len:21]
    elif code_len > 6 and code_len <= 9:
        code_form = code_str[16 - code_len:21]
    elif code_len > 9 and code_len <= 12:
        code_form = code_str[15 - code_len:21]
    elif code_len > 12 and code_len <= 14:
        code_form = code_str[14 - code_len:21]
    return code_form

class clv_person_mng(osv.osv):
    _inherit = 'clv_person_mng'

    _columns = {
        'person_code': fields.char('Person Code', size=64, select=1, required=False, readonly=False, default='/',
                                   help='Use "/" to get an automatic new Person Code.'),
        'family_code': fields.char('Family Code', size=64, select=1, required=False, readonly=False, default='/',
                                   help='Use "/" to get an automatic new Family Code.'),
        'patient_code': fields.char('Patient Code', size=64, select=1, required=False, readonly=False, default='/',
                                   help='Use "/" to get an automatic new Patient Code.'),
        }
    
    def write(self, cr, uid, ids, vals, context=None):
        if context is None:
            context = {}
        if ('person_code' in vals and vals['person_code'] == '/'):
            code_seq = self.pool.get('ir.sequence').get(cr, uid, 'clv_person.code')
            vals['person_code'] = format_code(code_seq)
        if ('family_code' in vals and vals['family_code'] == '/'):
            code_seq = self.pool.get('ir.sequence').get(cr, uid, 'clv_family.code')
            vals['family_code'] = format_code(code_seq)
        if ('patient_code' in vals and vals['patient_code'] == '/'):
            code_seq = self.pool.get('ir.sequence').get(cr, uid, 'clv_patient.code')
            vals['patient_code'] = format_code(code_seq)
        return super(clv_person_mng, self).write(cr, uid, ids, vals, context)
