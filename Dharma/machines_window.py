from gi.repository import Adw
from gi.repository import Gtk


from .singleton import singleton
from .guest.virtual import VirtualMachineManager
from .machine_row import DharmaMachineRow

@singleton
@Gtk.Template.from_file('gtk/machine-list-window.ui')
class DharmaMachinesWindow(Adw.Window):
    __gtype_name__ = "DharmaMachinesWindow"

    machines_list = Gtk.Template.Child()

    def __init__(self, parent: Adw.ApplicationWindow, manager: VirtualMachineManager) -> None:
        super().__init__()

        self.set_transient_for(parent)
        print(manager.instances)
        
        for instance in manager.instances:
            self.machines_list.add(DharmaMachineRow(instance, manager.open_viewer))
            
        self.present()
