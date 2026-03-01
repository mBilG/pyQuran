# desktop_view.py
#
# Copyright 2026 mBilG
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later


from gi.repository import Gtk

from .app_logic import PageInfo as pg

@Gtk.Template(resource_path='/com/thinqrlab/pyQuran/ui/desktop-view.ui')
class DesktopView(Gtk.Box):
    __gtype_name__ = 'DesktopView'

    view_double = Gtk.Template.Child()
    imageLeft = Gtk.Template.Child()
    imageRight = Gtk.Template.Child()
    labelLeft = Gtk.Template.Child()
    labelRight = Gtk.Template.Child()

    def __init__(self, **kwargs):
        self.init_template()


    def add_images(self, page_left, page_right, page_style, dark_mode=True):
        self.imageLeft.set_filename(pg.single_path_from_page(self, page_left, page_style, dark_mode))
        self.labelLeft.set_label(str(page_left))
        self.imageRight.set_filename(pg.single_path_from_page(self, page_right, page_style, dark_mode))
        self.labelRight.set_label(str(page_right))


