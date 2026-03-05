# mobile_view.py
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

import threading
from gi.repository import Gtk, Gio, GLib

from .page_info import GetPath
from .invert import get_texture

@Gtk.Template(resource_path='/com/thinqrlab/pyQuran/ui/mobile-view.ui')
class MobileView(Gtk.Box):
    __gtype_name__ = 'MobileView'

    view_single = Gtk.Template.Child()
    page = Gtk.Template.Child()

    def __init__(self, **kwargs):
        self.init_template()
        self.settings = Gio.Settings(schema_id='com.thinqrlab.pyQuran')


    def add_images(self, page_name):
        variant = self.settings.get_int("variant")
        dark_mode = self.settings.get_boolean("dark-mode")

        def background_work():
            texture = get_texture(GetPath.single(self, page_name, variant), invert=dark_mode)

            GLib.idle_add(self.page.set_paintable, texture)
        thread = threading.Thread(target=background_work, daemon=True)
        thread.start()







