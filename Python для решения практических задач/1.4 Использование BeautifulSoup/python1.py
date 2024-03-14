"""BeautifulSoup."""
from urllib.request import urlopen

from bs4 import BeautifulSoup

TASK = 3


def main():
    """My function."""
    urls = ("https://stepik.org/media/attachments/lesson/209723/3.html",
            "https://stepik.org/media/attachments/lesson/209723/4.html",
            "https://stepik.org/media/attachments/lesson/209723/5.html")
    with urlopen(urls[TASK - 1]) as response:  # скачиваем файл
        html = response.read().decode("utf8")  # считываем содержимое
    soup = BeautifulSoup(html, "html5lib")  # делаем суп
    print(sum(int(tag.get_text()) for tag in soup.find_all(["td", "th"])))


if __name__ == "__main__":
    main()
