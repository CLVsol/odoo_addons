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

class clv_medicament_template(osv.Model):
    _name = 'clv_medicament.template'

    _columns = {
        'name': fields.char(string='Medicament Template Code', size=64, required=True,  
                            help='Medicament Template Code'),
        'medicament': fields.many2one('clv_medicament', string='Medicament', required=True, 
                                      help='Prescribed Medicament'),
        'form': fields.many2one('clv_medicament.form', string='Form', 
                                help='Medicament form, such as tablet or gel'),
        'route': fields.many2one('clv_medicament.route', string='Administration Route', 
                                 help='Medicament administration route code.'),
        'dose': fields.float(string='Dose', 
                             help='Amount of medicament (eg, 250 mg) per dose'),
        'dose_unit': fields.many2one('product.uom', string='dose unit', 
                                     help='Unit of measure for the medicament to be taken'),
        'quantity': fields.integer(string='Medicament Quantity',
                                   help='Quantity of units (eg, 2 capsules) of the medicament'),
        'frequency': fields.integer(string='Frequency', 
                                    help='Time in between doses the patient must wait (ie, for 1 pill'\
                                          ' each 8 hours, put here 8 and select \"hours\" in the unit field'),
        'frequency_unit': fields.selection([('seconds', 'seconds'),
                                            ('minutes', 'minutes'),
                                            ('hours', 'hours'),
                                            ('days', 'days'),
                                            ('weeks', 'weeks'),
                                            ('wr', 'when required'),
                                            ], string='frequency unit',select=True, sort=False),
        'duration': fields.integer(string='Treatment duration',
                                   help='Period that the patient must take the medicament. in minutes, '\
                                        'hours, days, months, years or indefinately'),
        'duration_period': fields.selection([('minutes', 'minutes'),
                                             ('hours', 'hours'),
                                             ('days', 'days'),
                                             ('weeks', 'weeks'),
                                             ('months', 'months'),
                                             ('years', 'years'),
                                             ('indefinite', 'indefinite'),
                                             ('continuous use', 'continuous use'),
                                             ], string='Treatment period',
                                            help='Period that the patient must take the medicament in minutes,'\
                                                 ' hours, days, months, years or indefinately'),
        'admin_times': fields.char(size=256, string='Administration hours', 
                                   help='Suggested administration hours. For example, at 08:00, 13:00'\
                                        ' and 18:00 can be encoded like 08 13 18'),
        'active': fields.boolean('Active', 
                                 help="The active field allows you to hide the medicament template without removing it."),
        }

    _order='name'

    _sql_constraints = [('medicamente_template_name_uniq', 'unique(name)', u'Duplicated Medicamente Template Name!')]

    _defaults = {
        'active': 1,
    }
    