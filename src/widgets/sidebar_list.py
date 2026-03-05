# sidebar_list.py
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

from gi.repository import Gtk, GObject, Gio

from .sidebar_row import SidebarRow, DataItem

from .quran_data import surahStartPage
from .page_info import GetIndex


@Gtk.Template(resource_path='/com/thinqrlab/pyQuran/ui/sidebar-list.ui')
class SidebarList(Gtk.Box):
    __gtype_name__ = 'SidebarList'

    __gsignals__ = {
        'page-changed': (GObject.SignalFlags.RUN_FIRST, None, (str,))
    }

    listbox = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_template()
        self.ignore_signals = False

        self.model = Gio.ListStore.new(DataItem)
        self.listbox.bind_model(self.model, self.create_row)

        # Populate with 114 items
        for i in range(0, 114):
            self.model.append(DataItem(value=i))

    def create_row(self, item):
        return SidebarRow(item=item)

    @Gtk.Template.Callback()
    def on_row_selected(self, *args):
        if self.ignore_signals:
                return
        index = self.listbox.get_selected_row().get_index()
        i = surahStartPage[index]
        self.emit('page-changed', i)

    def highlight_row(self, page):
        i = GetIndex.get_first_index(surahStartPage, page)
        row = self.listbox.get_row_at_index(i)
        if row:
            self.ignore_signals = True
            self.listbox.select_row(row)
            self.ignore_signals = False




