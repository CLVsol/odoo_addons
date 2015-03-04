# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).                        #
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

from openerp import tools, api
from openerp.osv import osv, fields

ADDRESS_FORMAT_LAYOUTS = {
    '%(city)s %(state_code)s\n%(zip)s': """
        <div class="address_format">
            <field name="city" placeholder="%(city)s" style="width: 50%%"/>
            <field name="state_id" class="oe_no_button" placeholder="%(state)s" style="width: 47%%" options='{"no_open": true}'/>
            <br/>
            <field name="zip" placeholder="%(zip)s"/>
        </div>
    """,
    '%(zip)s %(city)s': """
        <div class="address_format">
            <field name="zip" placeholder="%(zip)s" style="width: 40%%"/>
            <field name="city" placeholder="%(city)s" style="width: 57%%"/>
            <br/>
            <field name="state_id" class="oe_no_button" placeholder="%(state)s" options='{"no_open": true}'/>
        </div>
    """,
    '%(city)s\n%(state_name)s\n%(zip)s': """
        <div class="address_format">
            <field name="city" placeholder="%(city)s"/>
            <field name="state_id" class="oe_no_button" placeholder="%(state)s" options='{"no_open": true}'/>
            <field name="zip" placeholder="%(zip)s"/>
        </div>
    """
}

class format_address(object):
    @api.model
    def fields_view_get_address(self, arch):
        fmt = self.env.user.company_id.country_id.address_format or ''
        for k, v in ADDRESS_FORMAT_LAYOUTS.items():
            if k in fmt:
                doc = etree.fromstring(arch)
                for node in doc.xpath("//div[@class='address_format']"):
                    tree = etree.fromstring(v % {'city': _('City'), 'zip': _('ZIP'), 'state': _('State')})
                    for child in node.xpath("//field"):
                        if child.attrib.get('modifiers'):
                            for field in tree.xpath("//field[@name='%s']" % child.attrib.get('name')):
                                field.attrib['modifiers'] = child.attrib.get('modifiers')
                    node.getparent().replace(node, tree)
                arch = etree.tostring(doc)
                break
        return arch

# fields copy if 'use_parent_address' is checked
ADDRESS_FIELDS = ('street', 'street2', 'zip', 'city', 'state_id', 'country_id')


class clv_address(osv.Model, format_address):
    _name = "clv_address"

    def _address_display(self, cr, uid, ids, name, args, context=None):
        res = {}
        for address in self.browse(cr, uid, ids, context=context):
            res[address.id] = self._display_address(cr, uid, address, context=context)
        return res

    _columns = {
        'name': fields.char('Name', required=True, select=True),
        'alias': fields.char('Alias', size=64, help='Common name that the Address is referred'),
        'code': fields.char(size=64, string='Address Code'),
        'notes': fields.text('Notes'),
        'street': fields.char('Street'),
        'street2': fields.char('Street2'),
        'zip': fields.char('Zip', size=24, change_default=True),
        'city': fields.char('City'),
        'state_id': fields.many2one("res.country.state", 'State', ondelete='restrict'),
        'country_id': fields.many2one('res.country', 'Country', ondelete='restrict'),
        'email': fields.char('Email'),
        'phone': fields.char('Phone'),
        'fax': fields.char('Fax'),
        'mobile': fields.char('Mobile'),
        'active': fields.boolean('Active', help="If unchecked, it will allow you to hide the address without removing it."),
        }

    _order = "name"

    def fields_view_get(self, cr, user, view_id=None, view_type='form', context=None, toolbar=False, submenu=False):
        if (not view_id) and (view_type=='form') and context and context.get('force_email', False):
            view_id = self.pool['ir.model.data'].get_object_reference(cr, user, 'base', 'view_address_simple_form')[1]
        res = super(clv_address,self).fields_view_get(cr, user, view_id, view_type, context, toolbar=toolbar, submenu=submenu)
        if view_type == 'form':
            res['arch'] = self.fields_view_get_address(cr, user, res['arch'], context=context)
        return res

    _defaults = {
        'active': True,
        }

    @api.multi
    def onchange_state(self, state_id):
        if state_id:
            state = self.env['res.country.state'].browse(state_id)
            return {'value': {'country_id': state.country_id.id}}
        return {}

    def _address_fields(self, cr, uid, context=None):
        """ Returns the list of address fields that are synced from the parent
        when the `use_parent_address` flag is set. """
        return list(ADDRESS_FIELDS)

    def name_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if isinstance(ids, (int, long)):
            ids = [ids]
        res = []
        for record in self.browse(cr, uid, ids, context=context):
            name = record.name
            if context.get('show_address_only'):
                name = self._display_address(cr, uid, record, without_company=True, context=context)
            if context.get('show_address'):
                name = name + "\n" + self._display_address(cr, uid, record, without_company=True, context=context)
            name = name.replace('\n\n','\n')
            name = name.replace('\n\n','\n')
            if context.get('show_email') and record.email:
                name = "%s <%s>" % (name, record.email)
            res.append((record.id, name))
        return res

    def _parse_address_name(self, text, context=None):
        """ Supported syntax:
            - 'Raoul <raoul@grosbedon.fr>': will find name and email address
            - otherwise: default, everything is set as the name """
        emails = tools.email_split(text.replace(' ',','))
        if emails:
            email = emails[0]
            name = text[:text.index(email)].replace('"', '').replace('<', '').strip()
        else:
            name, email = text, ''
        return name, email

    @api.model
    @api.returns('self')
    def main_address(self):
        ''' Return the main address '''
        return self.env.ref('base.main_address')

    def _display_address(self, cr, uid, address, without_company=False, context=None):

        '''
        The purpose of this function is to build and return an address formatted accordingly to the
        standards of the country where it belongs.

        :param address: browse record of the clv_address to format
        :returns: the address formatted in a display that fit its country habits (or the default ones
            if not country is specified)
        :rtype: string
        '''

        # get the information that will be injected into the display format
        # get the address format
        address_format = address.country_id.address_format or \
              "%(street)s\n%(street2)s\n%(city)s %(state_code)s %(zip)s\n%(country_name)s"
        args = {
            'state_code': address.state_id.code or '',
            'state_name': address.state_id.name or '',
            'country_code': address.country_id.code or '',
            'country_name': address.country_id.name or '',
        }
        for field in self._address_fields(cr, uid, context=context):
            args[field] = getattr(address, field) or ''
        if without_company:
            args['company_name'] = ''
        return address_format % args
