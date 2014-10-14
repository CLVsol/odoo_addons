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

class oehealth_pbm_insured_code(osv.osv):
    _description = 'Insured Codes'
    _name = 'oehealth.pbm.insured.code'

    def _compute_code_str(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        for r in self.browse(cr, uid, ids, context=context):
            code = map(int, str(r.code_number))
            while len(code) < 9:
                code.insert(0, 0)
            while len(code) < 11:
                n = sum([(len(code) + 1 - i) * v for i, v in enumerate(code)]) % 8
                if n > 1:
                    f = 8 - n
                else:
                    f = 0
                code.append(f)
            result[r.id] = "%s.%s-%s" % (str(code[3]) + str(code[4]) + str(code[5]), 
                                         str(code[6]) + str(code[7]) + str(code[8]),
                                         str(code[9]) + str(code[10]))
        return result

    _columns = {
        'name': fields.function(_compute_code_str, method=True, type='char', size=14, string='Insured Code',),
        'code_number' : fields.integer('Code Number'),
        'active': fields.boolean('Active', help="The active field allows you to hide the code without removing it."),
        'notes': fields.text('Notes'),
        }
    
    _order='code_number'

    _sql_constraints = [('pbm_insured_code_uniq', 'unique(code_number)', u'Duplicate Insured Code!')]

    _defaults = {
                 'active': True,
                 }

