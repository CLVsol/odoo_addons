
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

class oehealth_borderaux_row(osv.Model):
    _name = 'oehealth.borderaux.row'
    _description = "Borderaux Row"

    def _compute_create_uid(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        for r in self.browse(cr, uid, ids, context=context):
            perms = self.perm_read(cr, uid, ids)
            create_uid = perms[0].get('create_uid', 'n/a')
            result[r.id] = create_uid
        return result

    def _compute_create_date(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        for r in self.browse(cr, uid, ids, context=context):
            perms = self.perm_read(cr, uid, ids)
            create_date = perms[0].get('create_date', 'n/a')
            result[r.id] = create_date
        return result

    def _compute_write_uid(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        for r in self.browse(cr, uid, ids, context=context):
            perms = self.perm_read(cr, uid, ids)
            write_uid = perms[0].get('write_uid', 'n/a')
            result[r.id] = write_uid
        return result

    def _compute_write_date(self, cr, uid, ids, field_name, arg, context={}):
        result = {}
        for r in self.browse(cr, uid, ids, context=context):
            perms = self.perm_read(cr, uid, ids)
            write_date = perms[0].get('write_date', 'n/a')
            result[r.id] = write_date
        return result

    _columns = {
        'borderaux_number' : fields.char('Borderaux_no', size=64),
        'data_limite_uso_medicamento' : fields.date('Data_Limite_Uso_Medicamento'),
        'uso_continuo' : fields.char('UsoContinuo', size=254),
        'medida_dia' : fields.char('Medida_Dia', size=254),
        'unidade_dia' : fields.char('Unidade_Dia', size=254),
        'cod_prescritor' : fields.char('Cod_Prescritor', size=254),
        'bor' : fields.char('BOR', size=254),
        'numero_autoriz' : fields.char('Numero_AUTORIZ', size=254),
        'data_venda' : fields.date('DATA_VENDA'),
        'card_number' : fields.char('No_DO_CARTAO', size=254),
        'code' : fields.char('CODIGO', size=254),
        'up' : fields.char('UP', size=254),
        'quant' : fields.char('QUANT', size=254),
        'produto_garantemed' : fields.char('PRODUTO_GARANTEMED', size=254),
        'uc' : fields.char('UC', size=254),
        'preco_consumidor' : fields.char('PRECO_CONSUMIDOR', size=254),
        'custo_fcia' : fields.char('CUSTO_FCIA', size=254),
        'pr_vda_sist' : fields.char('PR_VDA_SIST', size=254),
        'receb_usuar' : fields.char('RECEB_USUAR', size=254),
        'saldo_a_receb' : fields.char('SALDO_A_RECEB', size=254),
        'a_receber' : fields.char('A_RECEBER', size=254),
        'prazo_compra' : fields.char('PRAZO_COMPRA', size=254),
        'usuario' : fields.char('USUARIO', size=254),
        'origem' : fields.char('ORIGEM', size=254),
        'crm_sp' : fields.char('CRM_SP', size=254),
        'principio_ativo' : fields.char('PRINCIPIO_ATIVO', size=254),
        'forma' : fields.char('FORMA', size=254),
        'preco_normal' : fields.char('PRECO_NORMAL', size=254),
        #'preco_normal': fields.float('PRECO_NORMAL'),
        'tipo' : fields.char('TIPO', size=254),
        'pr_garantemed' : fields.char('PR_GARANTEMED', size=254),
        'estornado': fields.boolean('Estornado'),
        'total_autori' : fields.char('TOTAL_AUTORI', size=254),
        'borderaux_id' : fields.many2one('oehealth.borderaux', 'Borderaux'),
        'authorization_id' : fields.many2one('oehealth.authorization', 'Authorization'),
        'prescriber_id' : fields.many2one('oehealth.prescriber', 'Prescriber'),
        'insured_card_id' : fields.many2one('oehealth.insured.card', 'Insured Card'),
        'insured_id' : fields.many2one('oehealth.insured', 'Insured'),
        'patient_id' : fields.many2one('oehealth.patient', 'Patient'),
        'gm_authorization': fields.related('authorization_id', 'gm_authorization_code', type='char', string='GM Authorization', 
                                       readonly=True, store=True),
        'medicament_id' : fields.many2one('oehealth.medicament', 'Medicament'),
        'category_ids': fields.many2many('oehealth.borderaux.row.category', 
                                         'oehealth_borderaux_row_category_rel', 
                                         'borderaux_row_id', 
                                         'category_id', 
                                         'Categories'),
        'tag_ids': fields.many2many('oehealth.tag', 
                                    'oehealth_borderaux_row_tag_rel', 
                                    'borderaux_row_id', 
                                    'tag_id', 
                                    'Tags'),
        'borderaux_row_info': fields.text(string='Borderaux Row Info'),
        'annotation_ids': fields.one2many('oehealth.annotation',
                                          'borderaux_row_id',
                                          'Annotations'),
        'state': fields.selection([('new','New'),
                                   ('revised','Revised'),
                                   ('waiting','Waiting'),
                                   ('okay','Okay')], 'Stage', readonly=True),
        'active': fields.boolean('Active', 
                                 help="The active field allows you to hide the borderaux row without removing it."),
        'create_uid': fields.function(_compute_create_uid, method=True, type='char', string='Create User',),
        'create_date': fields.function(_compute_create_date, method=True, type='datetime', string='Create Date',),
        'write_uid': fields.function(_compute_write_uid, method=True, type='char', string='Write User',),
        'write_date': fields.function(_compute_write_date, method=True, type='datetime', string='Write Date',),
    }

    #_order='name'

    #_sql_constraints = [('insurance_code_uniq', 'unique(insurance_code)', u'Duplicated Insurance Code!')]

    _defaults = {
        'active': 1,
        'state': 'new',
    }
    
    def oehealth_borderaux_row_new(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'new'})
         return True

    def oehealth_borderaux_row_revised(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'revised'})
         return True

    def oehealth_borderaux_row_waiting(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'waiting'})
         return True

    def oehealth_borderaux_row_okay(self, cr, uid, ids):
         self.write(cr, uid, ids, {'state': 'okay'})
         return True

oehealth_borderaux_row()
