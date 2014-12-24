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

from osv import osv
from osv import fields

class oehealth_abcfarma(osv.Model):
    _name = 'clv_abcfarma'

    def _compute_name(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        for r in self.browse(cr, uid, ids, context=context):
            result[r.id] = '[' + r.med_abc + '] ' + r.med_des + ' (' + r.med_princi + ') ' + r.med_apr + ' - ' + r.lab_nom + \
                           ' [' + r.med_barra + '] '
        return result

    _columns = {
        'name' : fields.function(_compute_name, method=True, type='char', size=128, string='ABCFarma Description',),
		'med_abc': fields.char(size=9, string='MED_ABC'),
		'med_ctr': fields.char(size=1, string='MED_CTR'),
		'med_lab': fields.char(size=6, string='MED_LAB'),
		'lab_nom': fields.char(size=30, string='LAB_NOM'),
		'med_des': fields.char(size=45, string='MED_DES'),
		'med_apr': fields.char(size=45, string='MED_APR'),
		'med_pco18': fields.float(string='MED_PCO18'),
		'med_pla18': fields.float(string='MED_PLA18'),
		'med_fra18': fields.float(string='MED_FRA18'),
		'med_pco17': fields.float(string='MED_PCO17'),
		'med_pla17': fields.float(string='MED_PLA17'),
		'med_fra17': fields.float(string='MED_FRA17'),
		'med_pco12': fields.float(string='MED_PCO12'),
		'med_pla12': fields.float(string='MED_PLA12'),
		'med_fra12': fields.float(string='MED_FRA12'),
		'med_uni': fields.float(string='MED_UNI'),
		'med_ipi': fields.float(string='MED_IPI'),
		'med_dtvig': fields.date('MED_DTVIG'),
		'exp_13': fields.boolean('EXP_13'),
		'med_barra': fields.char(size=13, string='MED_BARRA'),
		'med_gene': fields.char(size=3, string='MED_GENE'),
		'med_negpos': fields.char(size=1, string='MED_NEGPOS'),
		'med_princi': fields.char(size=130, string='MED_PRINCI'),
		'med_pco19': fields.float(string='MED_PCO19'),
		'med_pla19': fields.float(string='MED_PLA19'),
		'med_fra19': fields.float(string='MED_FRA19'),
		'med_pcozfm': fields.float(string='MED_PCOZFM'),
		'med_plazfm': fields.float(string='MED_PLAZFM'),
		'med_frazfm': fields.float(string='MED_FRAZFM'),
		'med_pco0': fields.float(string='MED_PCO0'),
		'med_pla0': fields.float(string='MED_PLA0'),
		'med_fra0': fields.float(string='MED_FRA0'),
		'med_regims': fields.char(size=13, string='MED_REGIMS'),
		'med_varpre': fields.char(size=1, string='MED_VARPRE'),

		'from': fields.char(size=128, string='From'),
		'excluded': fields.boolean('Excluded'),
		'product_name': fields.char(size=256, string='Product Name'),

        'active': fields.boolean('Active', 
                                 help="If unchecked, it will allow you to hide the medicament without removing it."),
    }

    _order='med_abc'

    _sql_constraints = [('med_abc_uniq', 'unique(med_abc)', u'Duplicated ABCFARMA Code!')]

    _defaults = {
        'active': 1,
    }
