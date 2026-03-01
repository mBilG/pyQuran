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

from gi.repository import Gtk, GObject, Pango

from .quran_data import *

from .app_logic import GetIndex

@Gtk.Template(resource_path='/com/thinqrlab/pyQuran/ui/sidebar-list.ui')
class SidebarList(Gtk.Box):
    __gtype_name__ = 'SidebarList'

    __gsignals__ = {
        'page-changed': (GObject.SignalFlags.RUN_FIRST, None, (str,))
    }

    # Bind the widgets defined in sidebar-list.ui
    listbox = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_template()
        self.populate_surah_list()
        self.ignore_signals = False

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



    def populate_surah_list(self):
        font_attrs = self.make_font_attrs("KFGQPC Uthmanic Script HAFS", 14)
        #font_attrs = self.make_font_attrs("Aref Ruqaa Ink", 14)

        # generate list of all surahs
        for i, surah in enumerate(surahName_ar):
            ### --- ROW CONTENTS --- ###
            # label for surah number
            label_surahNum = Gtk.Label.new(str=f'{i+1}')
            #label_surahNum.set_width_chars(3)
            label_surahNum.set_xalign(xalign=0)
            label_surahNum.set_yalign(yalign=0.5)
            #label_surahNum.set_margin_start(0)
            #label_surahNum.set_margin_end(10)
            label_surahNum.add_css_class("title-3")

            # label for surah Transliteration
            label_surahName_tr = Gtk.Label.new(str=surahName_tr[i])
            label_surahName_tr.set_width_chars(12)
            label_surahName_tr.set_xalign(xalign=1)
            label_surahName_tr.add_css_class("caption")

            # label for surah in Arabic
            label_surahName = Gtk.Label.new(str=f'{surah}')
            label_surahName.set_xalign(xalign=1)
            label_surahName.set_hexpand(expand=True)
            label_surahName.add_css_class("caption-heading")
            label_surahName.set_attributes(font_attrs)

            row = Gtk.ListBoxRow.new()
            row_vbox = Gtk.Box.new(orientation=Gtk.Orientation.VERTICAL, spacing=6)
            row_vbox.set_margin_start(12)
            row_vbox.set_margin_end(12)
            row_vbox.append(child=label_surahName)
            row_vbox.append(child=label_surahName_tr)

            row_hbox = Gtk.Box.new(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
            row_hbox.set_margin_top(margin=6)
            row_hbox.set_margin_bottom(margin=6)
            row_hbox.append(child=label_surahNum)
            row_hbox.append(child=row_vbox)
            # add box to row
            row.set_child(child=row_hbox)
            # add row to list
            self.listbox.append(child=row)


    def make_font_attrs(self, family: str, size_pt: int) -> Pango.AttrList:
        attrs = Pango.AttrList()
        # Font family
        family_attr = Pango.attr_family_new(family)
        attrs.insert(family_attr)
        # Font size is in Pango units (points * Pango.SCALE)
        size_attr = Pango.attr_size_new(int(size_pt * Pango.SCALE))
        attrs.insert(size_attr)
         # Bold
        attrs.insert(Pango.attr_weight_new(Pango.Weight.BOLD))
        return attrs


