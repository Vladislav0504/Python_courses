"""API."""
from requests import get


def main():
    """My function."""
    with open("dataset_24476_3.txt", "r", encoding="utf8") as file:
        for line in file:
            url = "http://numbersapi.com/" + line.strip() + "/math?json"
            response = get(url, timeout=10)
            print("Interesting" if response.json()["found"] else "Boring")


if __name__ == "__main__":
    main()
