# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-TODAY OpenERP S.A. <http://www.openerp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from lxml import etree

from openerp.osv import fields, osv
from openerp.tools.translate import _

class clv_survey_name_wiz(osv.osv_memory):
    _name = 'clv_survey.name.wiz'

    _columns = {
        'clv_survey_id': fields.many2one('clv_survey', 'Survey', required=True, ondelete='cascade', domain= [('state', '=', 'open')]),
        'page_no': fields.integer('Page Number'),
        'note': fields.text("Description"),
        'page': fields.char('Page Position',size = 12),
        'transfer': fields.boolean('Page Transfer'),
        'store_ans': fields.text('Store Answer'),
        'response': fields.char('Answer',size=16)
    }
    _defaults = {
        'page_no': -1,
        'page': 'next',
        'transfer': 1,
        'response': 0,
        'clv_survey_id': lambda self,cr,uid,context:context.get('clv_survey_id',False),
        'store_ans': '{}' #Setting the default pattern as '{}' as the field is of type text. The field always gets the value in dict format
    }

    def fields_view_get(self, cr, uid, view_id=None, view_type='form', context=None, toolbar=False, submenu=False):
        res = super(clv_survey_name_wiz, self).fields_view_get(cr, uid, view_id=view_id, view_type=view_type, context=context, toolbar=toolbar, submenu=False)
        if uid != 1:
            clv_survey_obj = self.pool.get('clv_survey')
            line_ids = clv_survey_obj.search(cr, uid, [('invited_user_ids','in',uid)], context=context)
            domain = str([('id', 'in', line_ids)])
            doc = etree.XML(res['arch'])
            nodes = doc.xpath("//field[@name='clv_survey_id']")
            for node in nodes:
                node.set('domain', domain)
            res['arch'] = etree.tostring(doc)
        return res

    def action_next(self, cr, uid, ids, context=None):
        """
        Start the clv_survey, Increment in started clv_survey field but if set the max_response_limit of
        clv_survey then check the current user how many times start this clv_survey. if current user max_response_limit
        is reach then this user can not start this clv_survey(Raise Exception).
        """
        clv_survey_obj = self.pool.get('clv_survey')
        search_obj = self.pool.get('ir.ui.view')
        if context is None: context = {}

        this = self.browse(cr, uid, ids, context=context)[0]
        clv_survey_id = this.clv_survey_id.id
        context.update({'clv_survey_id': clv_survey_id, 'sur_name_id': this.id})
        cr.execute('select count(id) from clv_survey_history where user_id=%s\
                    and clv_survey_id=%s' % (uid,clv_survey_id))

        res = cr.fetchone()[0]
        sur_rec = clv_survey_obj.browse(cr,uid,clv_survey_id,context=context)
        if sur_rec.response_user and res >= sur_rec.response_user:
            raise osv.except_osv(_('Warning!'),_("You cannot give response for this clv_survey more than %s times.") % (sur_rec.response_user))

        if sur_rec.max_response_limit and sur_rec.max_response_limit <= sur_rec.tot_start_clv_survey:
            raise osv.except_osv(_('Warning!'),_("You cannot give more responses. Please contact the author of this clv_survey for further assistance."))

        search_id = search_obj.search(cr,uid,[('model','=','clv_survey.question.wiz'),('name','=','Survey Search')])
        return {
            'view_type': 'form',
            "view_mode": 'form',
            'res_model': 'clv_survey.question.wiz',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'search_view_id': search_id[0],
            'context': context
        }

    def on_change_clv_survey(self, cr, uid, ids, clv_survey_id, context=None):
        """
            on change event of clv_survey_id field, if note is available in selected clv_survey then display this note in note fields.
        """
        if not clv_survey_id:
            return {}
        notes = self.pool.get('clv_survey').read(cr, uid, clv_survey_id, ['note'])['note']
        return {'value': {'note': notes}}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
