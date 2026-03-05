# alert.py
#
# Copyright 2026 mBilG
#
# for the alert widget


from gi.repository import Gtk, Adw, GObject


@Gtk.Template(resource_path='/com/thinqrlab/pyQuran/ui/alert.ui')
class AlertDialog(Adw.AlertDialog):
    __gtype_name__ = 'AlertDialog'

    def __init__(self, heading: str = None, body: str = None, **kwargs):
        super().__init__(**kwargs)


        if heading:
            self.set_heading(heading)
        if body:
            self.set_body(body)


    def show_async(self, parent_window: Gtk.Window, callback=None):
        self.choose(parent_window, None, callback or self._default_callback)


    def _default_callback(self, alert, result):
        response = alert.choose_finish(result)


