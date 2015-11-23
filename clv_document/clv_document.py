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

from openerp import models, fields
from datetime import datetime


class clv_document(models.Model):
    _name = "clv_document"

    name = fields.Char('Document Code', size=128, help="Document result Code")
    doc_type = fields.Many2one('clv_document.type', 'Document type', help="Document type")
    # patient = fields.Many2one('clv_patient', 'Patient', help="Patient")
    # 'pathologist' : fields.many2one('clv_professional','Pathologist',help="Pathologist"),
    # 'requester' : fields.many2one('clv_professional', 'Doctor', help="Doctor who requested the test"),
    # results = fields.Text('Results')
    # diagnosis = fields.Text('Diagnosis')
    # criteria = fields.One2many('clv_document.criterion',
    #                            'document_id',
    #                            'Test Cases')
    date_requested = fields.Datetime('Date requested',
                                     default=lambda *a: datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    date_document = fields.Datetime('Document Date')
    responsible = fields.Many2one('res.users', 'Document Responsible', required=False, readonly=False)
    notes = fields.Text(string='Notes')
    active = fields.Boolean('Active',
                            help="If unchecked, it will allow you to hide the document without removing it.",
                            default=1)

    _sql_constraints = [('name_uniq', 'unique (name)', 'Error! The Document Code must be unique!')]

    _order = 'name'
