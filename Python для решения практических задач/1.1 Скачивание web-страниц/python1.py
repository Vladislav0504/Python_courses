"""Download web pages."""
from urllib.request import urlopen


def main():
    """My function."""
    url = "https://stepik.org/media/attachments/lesson/209717/1.html"
    with urlopen(url) as response:
        html = response.read().decode("utf8")
        print("C++" if html.count("C++") > html.count("Python") else "Python")


if __name__ == "__main__":
    main()
