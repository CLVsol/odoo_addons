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

class clv_document_document_question(osv.osv):
    _name = 'clv_document.document_question'

    _columns = {
        'document_id': fields.many2one('clv_document', string='Document',
                                        help='Document', required=False),
        'document_question_id': fields.many2one('clv_document.question', string='Document Question'),
        'answer': fields.many2one('clv_document.question_answer', 'Answer', required=False),
        'notes': fields.text(string='Notes'),
        'active': fields.boolean('Active', 
                                 help="If unchecked, it will allow you to hide the document_question without removing it."),
        }

    _defaults = {
        'active': 1,
        }
    
class clv_document(osv.osv):
    _inherit = 'clv_document'

    _columns = {
        'document_question_ids': fields.one2many('clv_document.document_question',
                                                 'document_id',
                                                 'Document Questions'),
    }

class clv_document_question(osv.osv):
    _inherit = 'clv_document.question'

    _columns = {
        'document_ids': fields.one2many('clv_document.document_question',
                                        'document_question_id',
                                        'Documents'),
        }

