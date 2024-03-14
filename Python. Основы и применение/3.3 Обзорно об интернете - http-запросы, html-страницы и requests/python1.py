"""Internet."""
from re import compile as re_compile

from typing import Pattern, AnyStr, Iterator

from requests import get


def help_url(pattern: Pattern[AnyStr], string: str) -> Iterator[str]:
    """Help url."""
    # в findall кортежи ("([^>]*? )*?", "(.*?)")
    lst = pattern.findall(string)
    yield from (url.replace("stepic.org", "stepik.org") for _, url in lst)


def main():
    """My function."""
    url_a, url_b, good_code = input(), input(), 200
    response = get(url_a, timeout=10)
    link_pattern = re_compile(r"<a ([^>]*? )*?href=\"(.*?)\"[^>]*?>")
    for url in help_url(link_pattern, response.text):
        response_2 = get(url, timeout=10)
        if response_2.status_code == good_code:
            if url_b in list(help_url(link_pattern, response_2.text)):
                print("Yes")
                break
    else:
        print("No")


if __name__ == "__main__":
    main()
