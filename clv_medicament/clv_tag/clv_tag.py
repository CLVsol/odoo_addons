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
        'medicament_ids': fields.many2many('clv_medicament', 
                                           'clv_medicament_clv_tag_rel', 
                                           'tag_id', 
                                           'medicament_id', 
                                           'Medicaments'),
        'medicament_manufacturer_ids': fields.many2many('clv_medicament.manufacturer', 
                                                        'clv_medicament_manufacturer_clv_tag_rel', 
                                                        'tag_id', 
                                                        'medicament_manufacturer_id', 
                                                        'Medicament Manufacturers'),
        'medicament_active_component_ids': fields.many2many('clv_medicament.active_component', 
                                                            'clv_medicament_active_component_clv_tag_rel', 
                                                            'tag_id', 
                                                            'medicament_active_component_id', 
                                                            'Medicament Active Components'),
        }

class clv_medicament(osv.osv):
    _inherit = 'clv_medicament'

    _columns = {
        'tag_ids': fields.many2many('clv_tag', 
                                    'clv_medicament_clv_tag_rel', 
                                    'medicament_id', 
                                    'tag_id', 
                                    'Tags'),
        }

class clv_medicament_manufacturer(osv.osv):
    _inherit = 'clv_medicament.manufacturer'

    _columns = {
        'tag_ids': fields.many2many('clv_tag', 
                                    'clv_medicament_manufacturer_clv_tag_rel', 
                                    'medicament_manufacturer_id', 
                                    'tag_id', 
                                    'Tags'),
        }

class clv_medicament_active_component(osv.osv):
    _inherit = 'clv_medicament.active_component'

    _columns = {
        'tag_ids': fields.many2many('clv_tag', 
                                    'clv_medicament_active_component_clv_tag_rel', 
                                    'medicament_active_component_id', 
                                    'tag_id', 
                                    'Tags'),
        }
