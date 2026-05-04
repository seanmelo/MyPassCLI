# import os
# from cryptography.fernet import Fernet
from vault import Vault


def welcome() -> None:
    print("Hello, Welcome to mypasswordcli")


def main():
    welcome()
    vault = Vault()
    while True:
        choice = input(
            "Enter 1 to add a login, 2 to fetch a login, any other input to save and quit"
        )
        match choice:
            case 1:
                name = input("Enter website name.")
                username = input(f"Enter username for {name}.")
                password = input(f"Enter password for {name}.")
                vault.add_entry(name, input, password)
            case 2:
                pass
            case _:
                break


if __name__ == "__main__":
    main()
