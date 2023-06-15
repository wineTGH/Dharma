import os

from gi.repository import Adw
from gi.repository import Gtk

from .accounts_list import DharmaAccountsList
from .filepath_settings import DharmaFilePathSettings
from .machines_window import DharmaMachinesWindow
from .guest.main import Dharma


@Gtk.Template.from_file("gtk/window.ui")
class DharmaWindow(Adw.ApplicationWindow):
    __gtype_name__ = "DharmaWindow"

    accounts_list = Gtk.Template.Child()
    qcow_file_button = Gtk.Template.Child()
    game_files_button = Gtk.Template.Child()
    run_button = Gtk.Template.Child()

    filepath_settings = None
    accounts_list_object = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.accounts_list_object = DharmaAccountsList(self.accounts_list, self)
        self.filepath_settings = DharmaFilePathSettings(
            self.qcow_file_button, self.game_files_button, self
        )
        self.run_button.connect("clicked", self.run)

    def run(self, button):
        dharma_main = Dharma(
            self.accounts_list_object.accounts,
            self.filepath_settings.qcow_image_path,
            self.filepath_settings.game_folder_path,
        )
        dharma_main.run_loop(2)
        DharmaMachinesWindow(self, dharma_main.manager)