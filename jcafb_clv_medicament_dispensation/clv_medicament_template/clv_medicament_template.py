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

class clv_medicament_template(osv.osv):
    _inherit = 'clv_medicament.template'

    _columns = {
        'question_01': fields.selection([('S', 'Sim'),
                                         ('N', 'Nao'),
                                         ], string='Receita válida',select=True, sort=False),
        'question_02': fields.char(size=256, string='Como foi prescrito na receita? (posologia, modo de uso)'),
        'question_03': fields.char(size=256, string='Onde o Sr.(a) adquire esse medicamento?'),
        'question_04': fields.char(size=256, string='Para que o Sr.(a) acha tem que tomar/utilizar este medicamento? (perguntar, não apenas ler na receita)'),
        'question_05': fields.char(size=256, string='Como o Sr.(a) conserva este medicamento?'),
        'question_06': fields.char(size=256, string='Como o Sr.(a) toma/utiliza este medicamento?* (perguntar, não apenas ler na receita)'),
        'question_07': fields.char(size=256, string='Quantas vezes o Sr.(a) esqueceu de tomar este medicamento nos últimos 15 dias?'),
        'question_08': fields.char(size=256, string='Há quanto tempo o Sr.(a) utiliza este medicamento? (pode-se colocar faixas de tempo)'),
        'question_09': fields.char(size=256, string='O medicamento está dentro do prazo de validade?'),
        'question_10': fields.selection([('S', 'Sim'),
                                         ('N', 'Nao'),
                                         ], string='Adere?',select=True, sort=False),
        'question_11': fields.char(size=256, string='Conhecimento sobre indicação?'),
        }
