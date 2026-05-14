import json
import os

# from cryptography.fernet import Fernet
from vault import Vault


def welcome() -> None:
    print("Hello, Welcome to mypasswordcli")


def main():
    welcome()
    # TODO: add json loading from local files and decryption
    vault = Vault()
    while True:
        choice = input(
            "Enter 1 to add a login, 2 to fetch a login, 3 to edit a login, 4 to delete a login, any other input to save and quit: "
        )
        match choice:
            case "1":
                name = input("Enter website name: ")
                username = input(f"Enter username for {name}: ")
                password = input(f"Enter password for {name}: ")
                vault.add_entry(name, username, password)
            case "2":
                name = input("Enter website name: ")
                username, password = vault.get(name)
                print(f"Username: {username}")
                print(f"Password: {password}")
            case "3":
                name = input("Enter name of entry to edit: ")
                new_username = input(
                    f"Enter new username for {name}. Press ENTER to skip: "
                )
                if new_username:
                    vault.edit_username(name, new_username)
                new_password = input(
                    f"Enter new password for {name}. Press ENTER to skip: "
                )
                if new_password:
                    vault.edit_password(name, new_password)
            case "4":
                name = input("Enter website name to delete: ")
                vault.remove_entry(name)

            case _:
                vault.dump()
                break


if __name__ == "__main__":
    main()
