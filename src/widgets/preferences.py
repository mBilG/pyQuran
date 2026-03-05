# preferences.py
#
# Copyright 2026 mBilG
#
# for the preferences window

from gi.repository import Adw, Gtk, Gio, GLib

import os
from pathlib import Path
import threading

from .alert import AlertDialog
from .quran_data import mushafVariant, githubLink
from .font_attr import FontAttr
from .page_info import GetPath, CheckPath, CheckFolder
from .downloader import FileDownloader, FileExtractor

@Gtk.Template(resource_path='/com/thinqrlab/pyQuran/ui/preferences.ui')
class PreferencesWindow(Adw.PreferencesWindow):
    __gtype_name__ = 'PreferencesWindow'


    dark_mode_switch = Gtk.Template.Child()
    combo_variant = Gtk.Template.Child()
    font_name = Gtk.Template.Child()
    font_size = Gtk.Template.Child()
    download_group = Gtk.Template.Child()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.combo_variant.set_model(Gtk.StringList.new(list(mushafVariant)))
        self.font_name.set_model(Gtk.StringList.new(FontAttr.font_list(self)))
        self.settings = Gio.Settings(schema_id='com.thinqrlab.pyQuran')
        self.style_manager = Adw.StyleManager.get_default()
        self.settings.bind("dark-mode", self.dark_mode_switch, "active", Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind("variant", self.combo_variant, "selected", Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind("font-name", self.font_name, "selected", Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind("font-size", self.font_size, "value", Gio.SettingsBindFlags.DEFAULT)
        self.settings.connect("changed::dark-mode", self.on_dark_mode_changed)
        self.font_name.connect("notify::selected", self.on_font_name_selected)
        self.font_size.connect("notify::value-changed", self.on_font_size_value_changed)
        self.combo_variant.connect("notify::selected", self.on_variant_value_changed)
        self.on_dark_mode_changed()
        self.font_name.set_selected(self.settings.get_int("font-name"))
        self.dl_worker = None
        self.ex_worker = None
        success, errors = CheckFolder.is_valid(f"{GLib.get_user_data_dir()}/mushaf")
        for i in errors:
            if i != "Hafs (Old)":
                self.add_download_row(i, "Not Downloaded", False)


    def add_download_row(self, folder_name: str, status_text: str, is_valid: bool):
            row = Adw.ActionRow()
            row.set_title(folder_name)
            row.set_subtitle(status_text)
            icon = Gtk.Image()
            icon.set_from_icon_name("dialog-error-symbolic")
            icon.add_css_class("error")
            row.add_prefix(icon)
            button_download = Gtk.Button()
            button_cancel = Gtk.Button()
            stack = Gtk.Stack(transition_type=Gtk.StackTransitionType.CROSSFADE)
            button_download.set_valign(Gtk.Align.CENTER)
            button_download.set_halign(Gtk.Align.CENTER)
            button_download.set_icon_name("folder-download-symbolic")
            button_download.add_css_class("flat")
            button_download.add_css_class("circular")
            button_download.connect("clicked", lambda btn: self._on_download_clicked(row, stack, folder_name))
            button_cancel.set_valign(Gtk.Align.CENTER)
            button_cancel.set_halign(Gtk.Align.CENTER)
            button_cancel.set_icon_name("am-dialog-error-symbolic")
            button_cancel.add_css_class("flat")
            button_cancel.add_css_class("circular")
            button_cancel.add_css_class("error")
            button_cancel.connect("clicked", lambda btn: self._on_cancel_clicked(row, stack, folder_name))
            stack.add_named(button_download, "download")
            stack.add_named(button_cancel, "cancel")
            row.add_suffix(stack)
            self.download_group.add(row)


    def on_dark_mode_changed(self, *args):
        """The actual logic to change the app appearance"""
        is_dark = self.settings.get_boolean("dark-mode")
        if is_dark:
            self.style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)
        else:
            self.style_manager.set_color_scheme(Adw.ColorScheme.FORCE_LIGHT)


    def on_font_name_selected(self, *args):
        self.settings.set_int("font-name", self.font_name.get_selected())


    def on_font_size_value_changed(self, *args):
        self.settings.set_int("font-size", int(self.font_size.get_selected()))


    def on_variant_value_changed(self, *args):
        i = self.combo_variant.get_selected()
        var = mushafVariant[i]

        if not CheckPath.is_valid(self, variant_id = i):
            dialog = AlertDialog(
                heading="Missing Variant",
                body=f"The variant: '{var}' needs to be downloaded first."
            )
            dialog.choose(self, None, self.on_alert_closed)
            self.settings.set_int("variant", 0)
        else:
            self.settings.set_int("variant", i)


    def on_alert_closed(self, alert, result):
        response = alert.choose_finish(result)


    def _on_download_clicked(self, row, stack, folder_name):
        self.row = row
        self.row.set_subtitle(f'Downloading: "{folder_name}"')
        stack.set_visible_child_name("cancel")

        url = githubLink[mushafVariant.index(folder_name)]
        cache = f"{GLib.get_user_cache_dir()}/com.thinqrlab.pyQuran"
        data = f"{GLib.get_user_data_dir()}/mushaf"

        self.dl_worker = FileDownloader(url, folder_name, cache, self.row)
        self.ex_worker = FileExtractor(cache, data, folder_name, self.row)

        threading.Thread(target=self.execute_sequence, daemon=True).start()


    def execute_sequence(self):
        if self.dl_worker.run():
            if self.ex_worker.run():
                GLib.idle_add(self.row.set_subtitle, "Status: Setup Complete")
                GLib.idle_add(self.download_group.remove, self.row)


    def _on_cancel_clicked(self, row, stack, folder_name):
        if self.dl_worker: self.dl_worker.cancel()
        if self.ex_worker: self.ex_worker.cancel()
        stack.set_visible_child_name("download")
        row.set_subtitle("Cancelled. Download again.")



