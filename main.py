# import os
# from cryptography.fernet import Fernet
from vault import Vault


def welcome() -> None:
    print("Hello, Welcome to mypasswordcli")


def main():
    welcome()
    vault = Vault()
    vault.add_entry("Google", "Joelikescybersecurity", "1337code")
    print(vault.table)


if __name__ == "__main__":
    main()
