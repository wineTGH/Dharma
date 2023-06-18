from gi.repository import Adw
from gi.repository import Gtk
from libvirt import virDomain
from os.path import dirname

@Gtk.Template.from_file(dirname(__file__) + "/gtk/machine-row.ui")
class DharmaMachineRow(Adw.ActionRow):
    __gtype_name__ = "DharmaMachineRow"
    
    open_view_button = Gtk.Template.Child()
    instance : virDomain

    def __init__(self, instance: virDomain, open_callback) -> None:
        super().__init__()
        self.instance = instance

        self.props.title = instance.name()
        self.props.subtitle = str(instance.state())
        
        self.open_view_button.connect("clicked", lambda _: open_callback(instance.name()))
