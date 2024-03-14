"""BeautifulSoup."""
from urllib.request import urlopen

from bs4 import BeautifulSoup


def main():
    """My function."""
    url = "https://stepik.org/media/attachments/lesson/245130/6.html"
    with urlopen(url) as response:  # скачиваем файл
        html = response.read().decode("utf8")  # считываем содержимое
    soup = BeautifulSoup(html, "html.parser")  # делаем суп
    count = 0
    for tag_tr in soup.find_all("tr"):
        count += 1
        for _ in tag_tr.find_all(["td", "th"]):
            count <<= 1
    print(count)


if __name__ == "__main__":
    main()
