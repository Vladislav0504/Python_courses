"""Html processing."""
from urllib.request import urlopen


def main():
    """My function."""
    url = "https://stepik.org/media/attachments/lesson/209719/2.html"
    with urlopen(url) as response:
        html = response.read().decode("utf8")
    count = {}
    start = html.find("<code>")
    end = html.find("</code>", start)
    while start != -1:
        text = html[start + len("<code>"):end]
        count[text] = count.get(text, 0) + 1
        start = html.find("<code>", end)
        end = html.find("</code>", start)
    maximum = max(count.values(), default=0)
    print(*sorted(key for key, value in count.items() if value == maximum))


if __name__ == "__main__":
    main()
