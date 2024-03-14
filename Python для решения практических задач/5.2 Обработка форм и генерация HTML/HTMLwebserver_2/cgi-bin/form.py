"""Form handler."""
from html import escape

from urllib.parse import parse_qs

from os import environ


def main():
    """My function."""
    form = parse_qs(environ["QUERY_STRING"])
    text = form.get("INPUT_TEXT", ["не задано"])[0]
    text = escape(text[:-1])

    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
                <html>
                <head>
                    <meta charset="utf-8">
                </head>
                <body>""")

    for char in text[1::2]:
        result = hash(char)
        print(f"<h1>{result}</h1>")

    print("""</body>
            </html>""")


if __name__ == "__main__":
    main()
