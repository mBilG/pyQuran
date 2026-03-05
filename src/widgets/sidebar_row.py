# sidebar_row.py
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

from gi.repository import Adw, Gtk, GObject, Gio

from .font_attr import FontAttr
from .quran_data import surahName_ar, surahName_tr

class DataItem(GObject.Object):
    def __init__(self, value: int):
        super().__init__()
        self.value = value

@Gtk.Template(resource_path='/com/thinqrlab/pyQuran/ui/sidebar-row.ui')
class SidebarRow(Adw.ActionRow):
    __gtype_name__ = 'SidebarRow'

    label_id = Gtk.Template.Child()
    label_name = Gtk.Template.Child()
    label_sub = Gtk.Template.Child()

    def __init__(self, item: DataItem, **kwargs):
        super().__init__(**kwargs)

        self.settings = Gio.Settings(schema_id='com.thinqrlab.pyQuran')
        self.settings.connect("changed::font-name", self._update_font_name)
        self.settings.connect("changed::font-size", self._update_font_size)

        i = item.value
        self.init_template()
        self.label_id.set_text(str(i))
        self.label_name.set_text(surahName_ar[i])
        self.label_sub.set_text(surahName_tr[i])
        self.update_row()


    def _update_font_name(self, settings, key, *args):
        self.update_row()

    def _update_font_size(self, settings, key, *args):
        self.update_row()


    def update_row(self):
        font_name = FontAttr.font_list(self)[self.settings.get_int("font-name")]
        font_size = self.settings.get_int("font-size")
        self.label_name.set_attributes(FontAttr.make_font_attrs(self, font_name, font_size))


