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
        'associate_oehealth_person': fields.boolean('Associate OeHealth Person', 
                                                    help="If checked, it will require to associate to a oehealth person."),
        'oehealth_person_id': fields.many2one('oehealth.person', 'Oehealth Person', ondelete='restrict'),

        'oehealth_spouse_id':  fields.many2one('oehealth.person', 'Spouse', ondelete='restrict'),
        'oehealth_father_id': fields.many2one('oehealth.person', 'Father', ondelete='restrict'),
        'oehealth_mother_id': fields.many2one('oehealth.person', 'Mother', ondelete='restrict'),
        'oehealth_responsible_id': fields.many2one('oehealth.person', 'Responsible', ondelete='restrict'),

        'associate_oehealth_partner': fields.boolean('Associate OeHealth Partner', 
                                                     help="If checked, it will require to associate to a oehealth partner."),
        'oehealth_partner_id': fields.many2one('res.partner', 'Oehealth Partner', ondelete='restrict'),
        }

    _defaults = {
        'associate_oehealth_person': 0,
        'associate_oehealth_partner': 0,
        }
