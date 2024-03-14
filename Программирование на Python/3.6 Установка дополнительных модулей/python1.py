"""Importing modules."""
from requests import get


def main():
    """My function."""
    with open("dataset_3378_2.txt", "r", encoding="utf8") as file:
        address = file.readline()
    file = get(address.strip(), timeout=10)
    print(len(file.text.splitlines()))


if __name__ == "__main__":
    main()
