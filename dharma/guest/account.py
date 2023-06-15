class DharmaAccount:
    username = None
    password = None
    secret_file = None

    # TODO: Implement this
    machine_ram = None
    machine_vcpu = None

    def __init__(self, username: str, password: str, secret_file: str) -> None:
        self.username = username
        self.password = password
        self.secret_file = secret_file

    def __str__(self) -> str:
        account_dict = {
            "username": self.username,
            "password": self.password,
            "secret_file": self.secret_file,
        }
        return str(f"DharmaAccount({account_dict})")

    def __repr__(self) -> str:
        return self.__str__()
