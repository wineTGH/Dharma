import subprocess

import libvirt


class VirtualMachineManager:
    instances = []

    def __init__(self) -> None:
        self.conn = libvirt.open("qemu:///system")
        if self.conn == None:
            raise ConnectionError()

    def createFromTemplate(
        self, template: str, template_variables: dict
    ) -> libvirt.virDomain:
        """
        Template variables example:

        ```python
        {
            '{%guest_name%}': 'test',
            '{%account_data%}': '/tmp',
            '{%host_game%}': '/tmp',
            '{%qcow_path%}': '/images/test.qcow2',
        }
        ```

        This wil create new instance with name `test`, image `test.qcow2`,
        game and account dir `/tmp`.
        """

        self.template_variables = template_variables.keys()

        for temp_var in self.template_variables:
            template = template.replace(temp_var, template_variables[temp_var])
        try:
            instance = self.conn.defineXML(template)
        except libvirt.libvirtError:
            instance = self.conn.lookupByName(template_variables.get("{%guest_name%}"))

        self.instances.append(instance)

        return instance

    def find(self, instance_name: str) -> libvirt.virDomain | None:
        for instance in self.instances:
            if instance.name() == instance_name:
                return instance
        return None

    def open_viewer(self, instance_name: str):
        subprocess.Popen(["virt-viewer", "--connect", "qemu:///system", instance_name])

    def run(self, instance: libvirt.virDomain):
        instance.create()

    def run(self, instance_name: str):
        instance = self.find(instance_name)
        if instance is None:
            return

        instance.create()
