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

from openerp.osv import orm, fields
from openerp import tools, api

class clv_file_image(orm.Model):
    _inherit = 'clv_file'

    @api.multi
    def _get_image(self, name, args):
        return dict((p.id, tools.image_get_resized_images(p.image)) for p in self)

    @api.one
    def _set_image(self, name, value, args):
        return self.write({'image': tools.image_resize_image_big(value)})

    @api.multi
    def _has_image(self, name, args):
        return dict((p.id, bool(p.image)) for p in self)

    _columns = {
        'image': fields.binary("Image",
                               help="This field holds the image used as avatar for this file, limited to 1024x1024px"),
        'image_medium': fields.function(_get_image, fnct_inv=_set_image,
                                        string="Medium-sized image", type="binary", multi="_get_image",
                                        store={
                                               'clv_file': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
                                               },
                                        help="Medium-sized image of this file. It is automatically "\
                                             "resized as a 128x128px image, with aspect ratio preserved. "\
                                             "Use this field in form views or some kanban views."
                                        ),
        'image_small': fields.function(_get_image, fnct_inv=_set_image,
                                       string="Small-sized image", type="binary", multi="_get_image",
                                       store={
                                              'clv_file': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
                                              },
                                       help="Small-sized image of this file. It is automatically "\
                                            "resized as a 64x64px image, with aspect ratio preserved. "\
                                            "Use this field anywhere a small image is required."),
        'has_image': fields.function(_has_image, type="boolean"),
    }
