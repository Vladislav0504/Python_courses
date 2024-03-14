"""Form handler."""
from html import escape

from urllib.parse import parse_qs

from os import environ


def my_hash(string: str) -> int:
    """My hash."""
    ans, num = 0, 123417
    for char in string:
        ans = ans * num + ord(char)
    return ans


def main():
    """My function."""
    form = parse_qs(environ["QUERY_STRING"])
    text = form.get("INPUT_TEXT", ["не задано"])[0]
    text = escape(text)

    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
                <html>
                <head>
                    <meta charset="utf-8">
                </head>
                <body>""")

    result = my_hash(text)
    print(f"<h1>{result}</h1>")

    print("""</body>
                </html>""")


if __name__ == "__main__":
    main()
