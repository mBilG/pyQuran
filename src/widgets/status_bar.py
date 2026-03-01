from gi.repository import Gtk, Adw

@Gtk.Template(resource_path='/com/thinqrlab/pyQuran/ui/status-bar.ui')
class StatusBar(Gtk.Box):
    __gtype_name__ = 'StatusBar'


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_template()

    def set_carousel(self, carousel):
        """Link the indicator to a specific carousel instance"""
        self.indicator.set_carousel(carousel)
