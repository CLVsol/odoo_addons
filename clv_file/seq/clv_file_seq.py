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

def format_code(code_seq, code_len):
    code = map(int, str(code_seq))
    while len(code) < 10:
        code.insert(0, 0)
    while len(code) < 12:
        n = sum([(len(code) + 1 - i) * v for i, v in enumerate(code)]) % 11
        if n > 1:
            f = 11 - n
        else:
            f = 0
        code.append(f)
    if code_len == 3:
        code_str = "%s%s" % (str(code[7]) + str(code[8]) + str(code[9]),
                             str(code[10]) + str(code[11]))
    elif code_len == 4:
        code_str = "%s%s%s" % (str(code[6]), 
                               str(code[7]) + str(code[8]) + str(code[9]),
                               str(code[10]) + str(code[11]))
    elif code_len == 6:
        code_str = "%s%s%s" % (str(code[4]) + str(code[5]) + str(code[6]),
                               str(code[7]) + str(code[8]) + str(code[9]),
                               str(code[10]) + str(code[11]))
    elif code_len == 9:
        code_str = "%s%s%s%s" % (str(code[1]) + str(code[2]) + str(code[3]),
                                 str(code[4]) + str(code[5]) + str(code[6]),
                                 str(code[7]) + str(code[8]) + str(code[9]),
                                 str(code[10]) + str(code[11]))
    elif code_len == 10:
        code_str = "%s%s%s%s%s" % (str(code[0]),
                                   str(code[1]) + str(code[2]) + str(code[3]),
                                   str(code[4]) + str(code[5]) + str(code[6]),
                                   str(code[7]) + str(code[8]) + str(code[9]),
                                   str(code[10]) + str(code[11]))
    return code_str

class clv_file(models.Model):
    _inherit = 'clv_file'

    code = fields.Char('File Code', size=64, select=1, required=False, readonly=False, default='/',
                       help='Use "/" to get an automatic new File Code.')
    code_size = fields.Selection([(3, 3),
                                  (4, 4),
                                  (6, 6),
                                  (9, 9),
                                  (10, 10),
                                  ], string='Code Size', select=True, sort=False, default=10)
    
    @api.model
    def create(self, vals):
        if not 'code' in vals or ('code' in vals and vals['code'] == '/'):
            if ('code_size' in vals and vals['code_size'] == 3):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code03')
            elif ('code_size' in vals and vals['code_size'] == 4):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code04')
            elif ('code_size' in vals and vals['code_size'] == 6):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code06')
            elif ('code_size' in vals and vals['code_size'] == 9):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code09')
            elif ('code_size' in vals and vals['code_size'] == 10):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code10')
            code_len = len(code_seq)
            vals['code'] = format_code(code_seq, code_len)
        return super(clv_file, self).create(vals)

    @api.multi
    def write(self, vals):
        if 'code' in vals and vals['code'] == '/':
            if ('code_size' in vals):
                code_len = vals['code_size']
            else:
                code_len = self.code_size
            if (code_len == 3):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code03')
            elif (code_len == 4):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code04')
            elif (code_len == 6):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code06')
            elif (code_len == 9):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code09')
            elif (code_len == 10):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code10')
            vals['code'] = format_code(code_seq, code_len)
        elif 'code_size' in vals:
            if (vals['code_size'] == 3):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code03')
            elif (vals['code_size'] == 4):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code04')
            elif (vals['code_size'] == 6):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code06')
            elif (vals['code_size'] == 9):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code09')
            elif (vals['code_size'] == 10):
                code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_file.code10')
            code_len = len(code_seq)
            vals['code'] = format_code(code_seq, code_len)
        return super(clv_file, self).write(vals)

    @api.one
    def copy(self, default=None):
        default = dict(default or {})
        default.update({'code': '/',})
        return super(clv_file, self).copy(default)
