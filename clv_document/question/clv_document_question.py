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

class clv_document(osv.osv):
    _name = 'clv_document.question'

    _columns = {
        'name': fields.char('Name', required=True, size=64),
        'alias': fields.char('Alias', size=64, help='Common name that the Document Question is referred'),
        'code': fields.char(size=64, string='Document Question Code', required=False),
        'description': fields.char(string='Description', size=256),
        'notes':  fields.text(string='Notes'),
        'active': fields.boolean('Active', 
                                 help="If unchecked, it will allow you to hide the document without removing it."),
        }

    _defaults = {
        'active': 1,
        }
    
    _sql_constraints = [('document_question_code_uniq', 'unique(code)', u'Error! The Document Question Code must be unique!')]

    _order='name'
