"""Internet."""
from re import findall, compile as re_compile

from requests import get


def main():
    """My function."""
    url_init, my_set = input(), set()
    response = get(url_init, timeout=10)
    pattern = r"<a ([^>]*? )*?href=(\"|\')(.*?)\2[^>]*?>"
    urls = findall(pattern, response.text)
    link_pattern = re_compile(r"(.*?://)?([\w.-]+).*")
    for _, _, url in urls:
        site = link_pattern.search(url).group(2)
        if site != "..":
            my_set.add(site)
    print(*sorted(my_set), sep="\n")


if __name__ == "__main__":
    main()
