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

from gi.repository import Adw, Gtk, Gio, GLib, GObject

import os, threading

from .desktop_view import DesktopView
from .mobile_view import MobileView
from .sidebar_list import SidebarList

from .quran_data import surahName_ar, surahStartPage

from .font_attr import FontAttr
from .page_info import GetIndex, CheckPath

Adw.init()

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
        self.settings = Gio.Settings(schema_id='com.thinqrlab.pyQuran')
        self.settings.connect("changed::dark-mode", self.update_ui_elements)
        self.settings.connect("changed::variant", self.on_variant_changed)
        self.sidebar_list.connect("page-changed", self._on_sidebar_selection)
        self.settings.connect("changed::font-name", self.update_font)
        self.settings.connect("changed::font-size", self.update_font)
        self.settings.set_int("variant", 0)
        self.page_spin.set_update_policy(Gtk.SpinButtonUpdatePolicy.IF_VALID)
        self.style_manager = Adw.StyleManager.get_default()
        self.style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK if self.settings.get_boolean("dark-mode") else Adw.ColorScheme.FORCE_LIGHT)
        page = self.settings.get_int("last-page")
        self.update_ui_elements()
        self.on_variant_changed()
        self.update_font()
        self.adjustment.set_value(page)
        self.update_display()


    @Gtk.Template.Callback()
    def on_adjustment_value_changed(self, *args):
        page_number = int(self.adjustment.get_value())
        self.update_display()
        self.sidebar_list.highlight_row(page_number)
        i = GetIndex.get_first_index(surahStartPage, page_number)
        if i < 114:
            self.app_title.set_label(surahName_ar[i])
        self.settings.set_int("last-page", page_number)


    @Gtk.Template.Callback()
    def on_btnLeft_clicked(self, *args):
        current_page = int(self.adjustment.get_value())
        view = self.view_stack.get_visible_child_name()
        if view == "mobile":
            self.adjustment.set_value(current_page + 1)
        if view == "desktop":
            self.adjustment.set_value(current_page + 2)


    @Gtk.Template.Callback()
    def on_btnRight_clicked(self, *args):
        current_page = int(self.adjustment.get_value())
        view = self.view_stack.get_visible_child_name()
        if view == "mobile":
            self.adjustment.set_value(current_page - 1)
        if view == "desktop":
            self.adjustment.set_value(current_page - 2)


    def _on_sidebar_selection(self, sidebar, page_number):
        self.adjustment.set_value(float(page_number))


    def update_ui_elements(self, *args):
        self.update_display()


    def on_variant_changed(self, *args):
        v = self.settings.get_int("variant")
        if CheckPath.is_valid(self, variant_id = v):
            self.update_display()


    def update_font(self, *args):
        font_name = FontAttr.font_list(self)[self.settings.get_int("font-name")]
        font_size = self.settings.get_int("font-size")
        font_attr = FontAttr.make_font_attrs(self, font_name, font_size)
        self.app_title.set_attributes(FontAttr.make_font_attrs(self, font_name, font_size))


    def update_display(self):
        page = int(self.adjustment.get_value())
        self.mobile_layout.add_images(page)
        self.desktop_layout.add_images(page)
