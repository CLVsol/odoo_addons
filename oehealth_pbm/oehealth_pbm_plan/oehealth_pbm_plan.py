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

class oehealth_pbm_plan(osv.Model):
    _name = 'oehealth.pbm.plan'

    _columns = {
        'name': fields.char(string='Name', size=264,required=True,  
                            help='Pharmacy Benefit Management plan'),
        #'is_default': fields.boolean(string='Default plan', 
        #                             help='Check if this is the default plan when assigning this PBM plan'\
        #                             ' company to a participant'),
        'company': fields.many2one('res.partner', string='PBM Plan Company',
                                   required=True),
        'alias': fields.char(string='Sigla', size=16, 
                             help='Sigla do Plano'),
        'cod_plan': fields.char(string='Cod. Plano', size=16, 
                                help='Código do Plano'),
        'cod_oper': fields.char(string='Cod. Operadora', size=16, 
                                help='Código da Operadora'),
        'notes': fields.text(string='Extra info'),
        #'plan': fields.many2one('product.product', string='Plan'),
    }

