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

class clv_tag(osv.osv):
    _inherit = 'clv_tag'

    _columns = {
        'person_mng_ids': fields.many2many('clv_person_mng', 
                                           'clv_person_mng_clv_tag_rel', 
                                           'tag_id', 
                                           'person_mng_id', 
                                           'Person Management'),
        }

class clv_person_mng(osv.osv):
    _inherit = 'clv_person_mng'

    _columns = {
        'tag_ids': fields.many2many('clv_tag', 
                                    'clv_person_mng_clv_tag_rel', 
                                    'person_mng_id', 
                                    'tag_id', 
                                    'Tags'),
        }
