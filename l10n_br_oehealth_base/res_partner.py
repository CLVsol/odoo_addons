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

import re
from openerp.osv import orm, fields

def validate_cpf(cpf):

    if not cpf.isdigit():
        cpf = re.sub('[^0-9]', '', cpf)
    if len(cpf) != 11:
        return False
    cpf = map(int, cpf)
    new = cpf[:9]
    while len(new) < 11:
        r = sum([(len(new) + 1 - i) * v for i, v in enumerate(new)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        new.append(f)
    if new == cpf:
        return True
    return False

class res_partner(orm.Model):
    _inherit = 'res.partner'

    _columns = {
        'cpf': fields.char('CPF', size=14),
        'rg': fields.char('RG', size=16),
        'rg_emitter': fields.char('RG Emitter', size=16),
    }

    def _check_cpf(self, cr, uid, ids):

        for partner in self.browse(cr, uid, ids):
            if not partner.cpf:
                continue
            if not validate_cpf(partner.cpf):
                return False
        return True

    _constraints = [
        (_check_cpf, u'CPF invalid!', ['cpf']),
    ]

    def onchange_mask_cnpj_cpf(self, cr, uid, ids, is_company, cnpj_cpf):
        result = super(res_partner, self).onchange_type(
            cr, uid, ids, is_company)
        if cnpj_cpf:
            val = re.sub('[^0-9]', '', cnpj_cpf)
            if is_company and len(val) == 14:
                cnpj_cpf = "%s.%s.%s/%s-%s"\
                % (val[0:2], val[2:5], val[5:8], val[8:12], val[12:14])
            elif not is_company and len(val) == 11:
                cnpj_cpf = "%s.%s.%s-%s"\
                % (val[0:3], val[3:6], val[6:9], val[9:11])
            result['value'].update({'cnpj_cpf': cnpj_cpf})
            if not is_company:
                result['value']['cpf'] = cnpj_cpf
        return result

    def onchange_mask_cpf(self, cr, uid, ids, is_company, cpf):
        result = super(res_partner, self).onchange_type(
            cr, uid, ids, is_company)
        if cpf:
            val = re.sub('[^0-9]', '', cpf)
            if len(val) == 11:
                cpf = "%s.%s.%s-%s" % (val[0:3], val[3:6], val[6:9], val[9:11])
            result['value'].update({'cpf': cpf})
        return result

res_partner()
