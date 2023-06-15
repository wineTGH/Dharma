from gi.repository import Adw
from gi.repository import Gtk

from account_row import DharmaAccountRow
from add_account_dialog import DharmaAddAccountDialog
from guest.account import DharmaAccount

class DharmaAccountsList():

    dialog_window = None
    gtk_template = None
    accounts = []

    def __init__(self, template, window) -> None:
        self.gtk_template = template
        self.app_window = window

        if type(self.gtk_template.get_header_suffix()) is Gtk.Button:
            self.gtk_template.get_header_suffix().connect("clicked", self.show_add_account_dialog)

    def show_add_account_dialog(self, button):
        self.dialog_window = DharmaAddAccountDialog(self.add_account_row, self.app_window)
        self.dialog_window.present()


    def add_account_row(self, account: DharmaAccount):
        account_row = DharmaAccountRow(self.delete_account, account)
        self.gtk_template.add(account_row)

        self.accounts.append(account)
        print(str(self.accounts))

    def delete_account(self, child: DharmaAccountRow):
        self.gtk_template.remove(child)

        self.accounts.remove(child.account)
        print(str(self.accounts))
