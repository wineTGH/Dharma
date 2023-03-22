from gi.repository import Adw
from gi.repository import Gtk


class DharmaFilePathSettings():
    parent_window = None

    qcow_image_path = None
    game_folder_path = None

    def __init__(self, qcow_button, game_button, parent_window) -> None:
        qcow_button.connect("clicked", self.qcow_filedialog)
        game_button.connect("clicked", self.game_filedialog)
        self.parent_window = parent_window

    def qcow_filedialog(self, button):
        def load_file(_dialog, response):

            """ Return if user cancels. """
            if response != Gtk.ResponseType.ACCEPT:
                return

            """ Run if the user selects an image. """
            self.qcow_image_path = dialog.get_file().get_path()

        dialog = Gtk.FileChooserNative.new(
            title=('Select an qcow image'),
            parent=self.parent_window,
            action=Gtk.FileChooserAction.OPEN
        )
        dialog.set_modal(True)
        dialog.connect('response', load_file)
        dialog.show()

    def game_filedialog(self, button):
        def load_file(_dialog, response):

            """ Return if user cancels. """
            if response != Gtk.ResponseType.ACCEPT:
                return

            """ Run if the user selects an game folder. """
            self.game_folder_path = dialog.get_file().get_path()

        dialog = Gtk.FileChooserNative.new(
            title=('Select an game folder'),
            parent=self.parent_window,
            action=Gtk.FileChooserAction.SELECT_FOLDER
        )
        dialog.set_modal(True)
        dialog.connect('response', load_file)
        dialog.show()
