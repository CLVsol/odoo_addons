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

class clv_insured(models.Model):
    _inherit = 'clv_insured'

    code = fields.Char('Insured Code', size=64, select=1, required=False, readonly=False, default='/',
                       help='Use "/" to get an automatic new Insured Code.')
    
    @api.model
    def create(self, vals):
        if not 'code' in vals or ('code' in vals and vals['code'] == '/'):
            code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_insured.code')
            vals['code'] = format_code(code_seq)
        return super(clv_insured, self).create(vals)

    @api.multi
    def write(self, vals):
        if 'code' in vals and vals['code'] == '/':
            code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_insured.code')
            vals['code'] = format_code(code_seq)
        return super(clv_insured, self).write(vals)

    @api.one
    def copy(self, default=None):
        default = dict(default or {})
        default.update({'code': '/',})
        return super(clv_insured, self).copy(default)
