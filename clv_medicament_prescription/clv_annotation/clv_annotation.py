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

class clv_medicament_prescription(osv.osv):
    _inherit = 'clv_medicament_prescription'

    _columns = {
        'annotation_ids': fields.many2many('clv_annotation', 
                                           'clv_medicament_prescription_annotation_rel', 
                                           'medicament_prescription_id', 
                                           'annotation_id', 
                                           'Annotations')
        }

class clv_annotation(osv.osv):
    _inherit = 'clv_annotation'

    _columns = {
        'medicament_prescription_ids': fields.many2many('clv_medicament_prescription', 
                                                        'clv_medicament_prescription_annotation_rel', 
                                                        'annotation_id', 
                                                        'medicament_prescription_id', 
                                                        'Medicament Prescriptions')
        }