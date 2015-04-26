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

class clv_medicament_manufacturer_str(osv.osv):
    _name = 'clv_medicament.manufacturer.str'

    _columns = {
        'name': fields.char(size=256, string='Manufacturer String', required=True),
        'manufacturer_id': fields.many2one('clv_medicament.manufacturer', string='Associated Manufacturer', 
                                           help='Associated Medicament Manufacturer'),
    }
    
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]

    _order='name'

class clv_medicament_manufacturer(osv.osv):
    _name = 'clv_medicament.manufacturer'

    def get_strings(self, cr, uid, ids, fields, arg, context):
        res={}
        for record in self.browse(cr, uid, ids, context=None):
            strings = ''
            for str_id in record.str_ids:
                if strings == '':
                    strings = str_id.name
                else:
                    strings = strings + '\n' + str_id.name
            res[record.id] = strings
        return res

    _columns = {
        'name': fields.char(size=256, string='Manufacturer', required=True),
        'code': fields.char(size=256, string='Code'),
        'info': fields.text(string='Info'),
        'active': fields.boolean('Active', help="The active field allows you to hide the manufacturer without removing it."),
        'medicament_ids': fields.one2many('clv_medicament', 'manufacturer', 'Medicaments'),
        'str_ids': fields.one2many('clv_medicament.manufacturer.str', 'manufacturer_id', 'Strings'),
        'strings' : fields.function(get_strings, method=True, string="Strings", type='char', store=False)
    }

    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
        ('code_uniq', 'UNIQUE(code)', 'Code must be unique!'),
    ]

    _order='name'

    _defaults = {
        'active': 1,
        }

class clv_medicament(osv.osv):
    _inherit = 'clv_medicament'

    _columns = {
        'manufacturer': fields.many2one('clv_medicament.manufacturer', string='Manufacturer', 
                                        help='Medicament Manufacturer'),
        }
    