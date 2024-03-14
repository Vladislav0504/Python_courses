"""Importing modules."""
from requests import get


def main():
    """My function."""
    url = "https://stepic.org/media/attachments/course67/3.6.3/"
    with open("dataset_3378_3.txt", "r", encoding="utf8") as file:
        address = file.readline().strip()
    string = get(address, timeout=10).text
    while string[:2] != "We":
        string = get((url + string).strip(), timeout=10).text
    with open("text2.txt", "w", encoding="utf8") as file:
        file.write(string)


if __name__ == "__main__":
    main()
