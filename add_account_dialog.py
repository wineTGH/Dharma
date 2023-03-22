from gi.repository import Adw
from gi.repository import Gtk

from dharma.account import DharmaAccount

@Gtk.Template.from_file('gtk/add-account-dialog.ui')
class DharmaAddAccountDialog (Adw.Window):
    __gtype_name__ = 'DharmaAddAccountDialog'
    
    parent_window = None
    add_callback = None

    add_account_button = Gtk.Template.Child()
    choose_secret_filedialog = Gtk.Template.Child()
    username_entry = Gtk.Template.Child()
    password_entry = Gtk.Template.Child()
    secrets_file_row = Gtk.Template.Child()

    secrets_file_path = None

    def __init__(self, add_callback, parent_window, account = None) -> None:
        super().__init__()
        self.set_transient_for(parent_window)
        self.choose_secret_filedialog.connect("clicked", self.open_file_dialog)
        self.add_account_button.connect("clicked", self.add_account)

        self.add_callback = add_callback

    def open_file_dialog(self, button):
        def load_file(_dialog, response):

            """ Return if user cancels. """
            if response != Gtk.ResponseType.ACCEPT:
                return

            """ Run if the user selects an secret file. """
            self.secrets_file_path = dialog.get_file().get_path()
            self.secrets_file_row.props.subtitle = dialog.get_file().get_basename()
        dialog = Gtk.FileChooserNative.new(
            title=('Select an secret file'),
            parent=self.parent_window,
            action=Gtk.FileChooserAction.OPEN
        )
        dialog.set_modal(True)
        dialog.connect('response', load_file)
        dialog.show()

    def add_account(self, button):
        
        account_username = self.username_entry.props.text
        account_password = self.password_entry.props.text
        account_secret_file = self.secrets_file_path

        if account_username == "": 
            print("Enter username")

        if account_password == "": 
            print("Enter password")

        if account_secret_file == "":
            print("Choose secret file")
        
        account = DharmaAccount(account_username, account_password, account_secret_file)

        self.add_callback(account)
        self.destroy()