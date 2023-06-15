from gi.repository import Adw
from gi.repository import Gtk

from guest.account import DharmaAccount

@Gtk.Template.from_file('gtk/account-row.ui')
class DharmaAccountRow (Adw.ActionRow):
    __gtype_name__ = 'DharmaAccountRow'

    delete_button = Gtk.Template.Child()
    delete_callback = None
    account = None

    def __init__(self, delete_callback, account: DharmaAccount) -> None:
        super().__init__()
        
        self.delete_callback = delete_callback
        self.account = account
        self.props.title = account.username
        
        if (type(self.delete_button) is Gtk.Button):
            self.delete_button.connect('clicked', self.delete_row)

    
    def delete_row(self, button):
        self.delete_callback(child=self)