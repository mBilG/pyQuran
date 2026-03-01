# window.py
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

from gi.repository import Adw, Gtk, Gdk, Pango, GLib

# custom widgets
from .desktop_view import DesktopView
from .mobile_view import MobileView
from .sidebar_list import SidebarList

from .app_logic import SaveState, GetIndex

from .quran_data import surahName_ar, surahStartPage

@Gtk.Template(resource_path='/com/thinqrlab/pyQuran/ui/window.ui')
class PyquranWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'PyquranWindow'

    desktop_layout = Gtk.Template.Child()
    mobile_layout = Gtk.Template.Child()

    main_toolbar_view = Gtk.Template.Child()
    split_view = Gtk.Template.Child()
    sidebar_list = Gtk.Template.Child()
    view_stack = Gtk.Template.Child()
    page_spin = Gtk.Template.Child()
    adjustment = Gtk.Template.Child()
    app_title = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sidebar_list.connect("page-changed", self._on_sidebar_selection)

        self.page_spin.set_update_policy(Gtk.SpinButtonUpdatePolicy.IF_VALID)
        self.page_spin.set_alignment(0.5)

        self.ss = SaveState(app_name="com.thinqrlab.pyQuran")
        page = self.ss.load_page()

        self.adjustment.set_value(page)
        self.update_display(page)
        self.set_title()


    @Gtk.Template.Callback()
    def on_adjustment_value_changed(self, *args):
        page_number = int(self.adjustment.get_value())
        self.update_display(page_number)
        self.ss.save_page(page_number)
        self.sidebar_list.highlight_row(page_number)
        font_attrs = self.sidebar_list.make_font_attrs("KFGQPC Uthmanic Script HAFS", 14)
        self.app_title.set_attributes(font_attrs)
        self.app_title.set_label(surahName_ar[GetIndex.get_first_index(surahStartPage, page_number)])


    @Gtk.Template.Callback()
    def on_btnLeft_clicked(self, *args):
        current_page = int(self.adjustment.get_value())
        view = self.view_stack.get_visible_child_name()
        if view == "mobile":
            self.adjustment.set_value(current_page+1)
        else:
            self.adjustment.set_value(current_page+2)

    @Gtk.Template.Callback()
    def on_btnRight_clicked(self, *args):
        current_page = int(self.adjustment.get_value())
        view = self.view_stack.get_visible_child_name()
        if view == "mobile":
            self.adjustment.set_value(current_page-1)
        else:
            self.adjustment.set_value(current_page-2)

    def _on_sidebar_selection(self, sidebar, page_number):
        self.adjustment.set_value(float(page_number))

    def check_dark_mode(self):
        self.dark_mode = Adw.StyleManager.get_dark(
                            Adw.StyleManager.get_default())
        if self.dark_mode == True:
            return "dark_mode"
        else:
            return "light_mode"


    def update_display(self, page):
        dark = self.check_dark_mode()
        self.mobile_layout.add_images(page, "old", dark_mode=dark)
        if page % 2 == 0:
            self.desktop_layout.add_images(page, page-1, "old", dark_mode=dark)
        else:
            self.desktop_layout.add_images(page+1, page, "old", dark_mode=dark)

