"""Modules and import."""
from simplecrypt import decrypt, DecryptionException


def main():
    """My function."""
    with open("encrypted.bin", "rb") as inp:
        encrypted = inp.read()
    with open("passwords.txt", "r", encoding="utf8") as file:
        for line in file:
            password = line.strip()
            try:
                string = decrypt(password, encrypted).decode("utf8")
                print(f"{password} is correct.")
                print(string)
                break
            except DecryptionException:
                print(f"{password} is wrong.")


if __name__ == "__main__":
    main()
