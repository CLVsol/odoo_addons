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
from datetime import datetime
from dateutil.relativedelta import relativedelta

class clv_person_mng(osv.osv):
    _inherit = 'clv_person_mng'

    _columns = {
        'associate_oehealth_patient': fields.boolean('Associate OeHealth Patient', 
                                                     help="If checked, it will require to associate to a oehealth patient."),
        'oehealth_patient_id': fields.many2one('oehealth.patient', 'Oehealth Patient', ondelete='restrict'),
        'oehealth_patient_category_ids': fields.many2many('oehealth.patient.category', 
                                                          'clv_person_mng_oehealth_patient_category_rel', 
                                                          'clv_person_mng_id', 
                                                          'category_id', 
                                                          'OeHealth Patient Categories'),
        } 

    _defaults = {
        'associate_oehealth_patient': 0,
        } 
