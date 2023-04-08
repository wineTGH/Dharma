import os
import subprocess
from shutil import copy, SameFileError

from dharma.virtual import VirtualMachineManager


class Dharma:
    manager: VirtualMachineManager
    accounts: list

    accounts_data_dir = "/home/winet/.dharma_tmp/accounts/"
    images_data_dir = "/home/winet/.dharma_tmp/images/"

    def __init__(
        self, accounts: list, qcow_base_image_path: str, game_folder_path: str
    ):
        self.accounts = accounts
        self.manager = VirtualMachineManager()

        if not os.path.exists(self.accounts_data_dir):
            os.makedirs(self.accounts_data_dir)

        if not os.path.exists(self.images_data_dir):
            os.makedirs(self.images_data_dir)

        for account in accounts:
            mount_dir = f"{self.accounts_data_dir}{account.username}"
            image_path = f"{self.images_data_dir}{account.username}.qcow2"

            try:
                os.mkdir(mount_dir)
            except FileExistsError:
                pass

            with open(f"{mount_dir}/login_info", "w") as f:
                f.write(f"{account.username}\n{account.password}")

            try:
                copy(account.secret_file, f"{mount_dir}/{account.username}.json")
            
            except SameFileError:
                pass
            subprocess.run(["genisoimage", "-o", f"{mount_dir}/{account.username}.iso", mount_dir])
            
            try:
                if not os.path.exists(image_path):
                    copy(qcow_base_image_path, image_path)
            except SameFileError:
                pass

            template_variables = {
                "{%guest_name%}": account.username,
                "{%account_data%}": f"{mount_dir}/{account.username}.iso",
                "{%qcow_path%}": image_path,
            }

            with open("dharma/template.xml") as f:
                self.manager.createFromTemplate(f.read(), template_variables.copy())

    def run_loop(self, process_cap: int):
        for instance in self.manager.instances:
            instance.create()
