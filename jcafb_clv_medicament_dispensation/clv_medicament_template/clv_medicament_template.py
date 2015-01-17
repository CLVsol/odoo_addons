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
        'question_02_01': fields.many2one('clv_medicament.route', string='Via de Administração', 
                                         help='oral/inalatória/tópica/oftálmica/otológica/intramuscular/subcutânea/intravenoso'),
        'question_02_02': fields.float(string='Dose', 
                             help='Amount of medicament (eg, 250 mg) per dose'),
        'question_02_03': fields.many2one('product.uom', string='Unidade da dose', 
                                     help='Unit of measure for the medicament to be taken'),
        'question_02_04': fields.char(size=256, string='Usar de quantas em quantas horas:'),
        'question_02_05': fields.selection([('a', 'a) Uso Contínuo'),
                                            ('b', 'b) Período Definido'),
                                            ('c', 'c) Uso somente em caso de necessidade (se dor, se febre, etc.'),
                                           ], string='Duração do Tratamento:',select=True, sort=False),
        'question_02_06': fields.char(size=256, string='Em caso de Período Definido, por quanto tempo?'),
        'question_02_07': fields.selection([('S', 'Sim'),
                                           ('N', 'Não'),
                                           ('X', 'Não se Aplica'),
                                           ], string='O Medicamento foi prescrito para uso em jejum?',select=True, sort=False),
        'question_02_08': fields.selection([('a', 'a) Com as refeições'),
                                            ('b', 'b) De manhã'),
                                            ('c', 'c) Com o almoço'),
                                            ('d', 'd) Antes de Dormir'),
                                            ('e', 'e) Não'),
                                            ], string='Medicamento foi prescrito para uso em horário determinado?',select=True, sort=False),
        'question_02_09': fields.char(size=256, string='Comentários sobre o modo de uso prescrito na receita:'), 
        'question_03': fields.selection([('a', 'a) Posto (UBS)'),
                                         ('b', 'b) Farmácia  Popular'),
                                         ('c', 'c) Compra na Farmácia'),
                                         ('d', 'd) Amostra de médico/farmacêutico'),
                                         ('e', 'e) Pega de alguém'),
                                         ('f', 'f) HC - Ribeirão Preto'),
                                         ('g', 'g) Outros'),
                                         ], string='Onde o Sr.(a) adquire esse medicamento?',select=True, sort=False),
        'question_04_01': fields.selection([('a', 'a) Hipertensão Arterial'),
                                         ('b', 'b) Diabetes'),
                                         ('c', 'c) Dislipidemia'),
                                         ('d', 'd) Próstata'),
                                         ('e', 'e) Depressão'),
                                         ('f', 'f) Tireóide'),
                                         ('g', 'g) Dor'),
                                         ('h', 'h) "Coração"'),
                                         ('i', 'i) "Cabeça"'),
                                         ('j', 'j) "Afinar o Sangue"'),
                                         ('k', 'k) Outros'),
                                         ], string='Para que o Sr.(a) acha tem que tomar/utilizar este medicamento?',select=True, sort=False),
        'question_04_02': fields.char(size=256, string='Em caso de outros, especifique:'),
        'question_05_01': fields.selection([('a', 'a) Dentro da Geladeira'),
                                            ('b', 'b) Cozinha/Banheiro'),
                                            ('c', 'c) Sala/Quarto'),
                                            ], string='Onde guarda o Medicamento?',select=True, sort=False),
        'question_05_02': fields.selection([('a', 'a) Fora do Blíster'),
                                            ('b', 'b) Blíster cortado nos potinhos das ACS'),
                                            ('c', 'c) Blíster cortado fora dos potinhos das ACS '),
                                            ('d', 'd) Blíster inteiro'),
                                            ('e', 'e) Não se Aplica'),
                                            ], string='Como conserva o Medicamento?',select=True, sort=False),
        'question_06_01': fields.many2one('clv_medicament.route', string='Via de Administração', 
                                         help='oral/inalatória/tópica/oftálmica/otológica/intramuscular/subcutânea/intravenoso'),
        'question_06_02': fields.float(string='Dose', 
                                       help='Amount of medicament (eg, 250 mg) per dose'),
        'question_06_03': fields.many2one('product.uom', string='Unidade da dose', 
                                     help='Unit of measure for the medicament to be taken'),
        'question_06_04': fields.char(size=256, string='Usa de quantas em quantas horas:'),
        'question_06_05': fields.selection([('a', 'a) Usa continuamente'),
                                            ('b', 'b) Usa por período definido'),
                                            ('c', 'c) Usa somente em caso de necessidade (se dor, se febre, etc.'),
                                           ], string='Duração do Tratamento:',select=True, sort=False),
        'question_06_06': fields.char(size=256, string='Em caso de Período Definido, por quanto tempo irá usar?'),
        'question_06_07': fields.selection([('S', 'Sim'),
                                            ('N', 'Não'),
                                            ('X', 'Não se Aplica'),
                                            ], string='O Medicamento está sendo usado em jejum?',select=True, sort=False),
        'question_06_08': fields.selection([('a', 'a) Com as refeições'),
                                            ('b', 'b) De manhã'),
                                            ('c', 'c) Com o almoço'),
                                            ('d', 'd) Antes de Dormir'),
                                            ('e', 'e) Não'),
                                            ('f', 'f) Não se aplica'),
                                            ], string='Medicamento está sendo usado em horário determinado?',select=True, sort=False),
        'question_06_09': fields.selection([('a', 'a) Até 3 meses'),
                                            ('b', 'b) 3 meses a 1 ano'),
                                            ('c', 'c) Mais que 1 ano'),
                                            ], string='Há quanto tempo o Sr.(a) utiliza este medicamento?',select=True, sort=False),
        'question_06_10': fields.char(size=256, string='Comentários sobre o modo de uso pelo paciente:'), 
        'question_06_11': fields.selection([('S', 'Sim'),
                                            ('N', 'Nao'),
                                            ], string='É condizente com o modo prescrito na receita?',select=True, sort=False),
        'question_07_01': fields.selection([('a', 'a) Nenhuma'),
                                            ('b', 'b) Até 3 vezes'),
                                            ('c', 'c) 4 ou mais vezes'),
                                            ], string='Quantas vezes o Sr.(a) esqueceu de tomar este medicamento nos últimos 15 dias?',select=True, sort=False),
        'question_07_02': fields.selection([('S', 'Sim'),
                                            ('N', 'Nao'),
                                            ], string='Adere?',select=True, sort=False),
        'question_08': fields.selection([('S', 'Sim'),
                                         ('N', 'Nao'),
                                         ], string='O medicamento está dentro do prazo de validade?',select=True, sort=False),
        'question_09': fields.selection([('S', 'Sim'),
                                         ('N', 'Nao'),
                                         ], string='Conhecimento sobre indicação?',select=True, sort=False),
        }
