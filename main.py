# import os
# from cryptography.fernet import Fernet


class Vault:
    def __init__(self):
        self.table = {}

    def add_entry(self, name: str, username: str, password: str) -> None:
        if name in self.table:
            print("Entry already exists. Overrwriting entry.")
        self.table[name] = {"username": username, "password": password}

    def remove_entry(self, name: str) -> None:
        if name in self.table:
            del self.table[name]
            print(f"Successfully deleted {name} and associated data.")
        else:
            print("Record not found.")

    def edit_password(self, name: str, password: str) -> None:
        if name in self.table:
            self.table[name]["password"] = password
        else:
            print("Record not found")

    def edit_username(self, name: str, username: str) -> None:
        if name in self.table:
            self.table[name]["username"] = username
        else:
            print("Record not found")


def welcome() -> None:
    print("Hello, Welcome to mypasswordcli")


def main():
    welcome()


if __name__ == "__main__":
    main()
