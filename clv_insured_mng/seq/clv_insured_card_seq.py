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

def format_crd_code(crd_code_seq):
    crd_code = map(int, str(crd_code_seq))
    crd_code_len = len(crd_code)
    while len(crd_code) < 14:
        crd_code.insert(0, 0)
    while len(crd_code) < 16:
        n = sum([(len(crd_code) + 1 - i) * v for i, v in enumerate(crd_code)]) % 11
        if n > 1:
            f = 11 - n
        else:
            f = 0
        crd_code.append(f)
    crd_code_str = "%s.%s.%s.%s.%s-%s" % (str(crd_code[0]) + str(crd_code[1]),
                                      str(crd_code[2]) + str(crd_code[3]) + str(crd_code[4]),
                                      str(crd_code[5]) + str(crd_code[6]) + str(crd_code[7]),
                                      str(crd_code[8]) + str(crd_code[9]) + str(crd_code[10]),
                                      str(crd_code[11]) + str(crd_code[12]) + str(crd_code[13]),
                                      str(crd_code[14]) + str(crd_code[15]))
    if crd_code_len <= 3:
        crd_code_form = crd_code_str[18 - crd_code_len:21]
    elif crd_code_len > 3 and crd_code_len <= 6:
        crd_code_form = crd_code_str[17 - crd_code_len:21]
    elif crd_code_len > 6 and crd_code_len <= 9:
        crd_code_form = crd_code_str[16 - crd_code_len:21]
    elif crd_code_len > 9 and crd_code_len <= 12:
        crd_code_form = crd_code_str[15 - crd_code_len:21]
    elif crd_code_len > 12 and crd_code_len <= 14:
        crd_code_form = crd_code_str[14 - crd_code_len:21]
    return crd_code_form

class clv_insured_mng(models.Model):
    _inherit = 'clv_insured_mng'

    # crd_code = fields.Char('Insured Card Code', size=64, select=1, required=False, readonly=False, default='/',
    #                    help='Use "/" to get an automatic new Insured Card Code.')
    
    @api.model
    def create(self, vals):
        if not 'crd_code' in vals or ('crd_code' in vals and vals['crd_code'] == '/'):
            crd_code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_insured_card.code')
            vals['crd_code'] = format_crd_code(crd_code_seq)
        return super(clv_insured_mng, self).create(vals)

    @api.multi
    def write(self, vals):
        if 'crd_code' in vals and vals['crd_code'] == '/':
            crd_code_seq = self.pool.get('ir.sequence').get(self._cr, self._uid, 'clv_insured_card.code')
            vals['crd_code'] = format_crd_code(crd_code_seq)
        return super(clv_insured_mng, self).write(vals)

    @api.one
    def copy(self, default=None):
        default = dict(default or {})
        default.update({'crd_code': '/',})
        return super(clv_insured_mng, self).copy(default)
