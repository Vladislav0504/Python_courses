"""Form handler."""
from html import escape

from urllib.parse import parse_qs

from os import environ


def main():
    """My function."""
    form = parse_qs(environ["QUERY_STRING"])
    text_1 = form.get("TEXT_1", ["не задано"])[0]
    text_2 = form.get("TEXT_2", ["не задано"])[0]
    text_1 = escape(text_1)
    text_2 = escape(text_2)

    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Обработка данных форм</title>
            </head>
            <body>""")

    print("<h1>Обработка данных форм!</h1>")
    print(f"<p>TEXT_1: {text_1}</p>")
    print(f"<p>TEXT_2: {text_2}</p>")

    print("""</body>
            </html>""")


if __name__ == "__main__":
    main()
