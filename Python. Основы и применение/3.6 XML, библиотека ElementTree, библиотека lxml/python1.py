"""XML."""
from xml.etree.ElementTree import fromstring, Element


def search(prices: dict[str, int], root: Element, price: int) -> None:
    """Depth-first search - DFS."""
    prices[root.attrib["color"]] += price
    for child in root:
        search(prices, child, price + 1)


def main():
    """My function."""
    prices = {"red": 0, "green": 0, "blue": 0}
    root = fromstring(input())
    search(prices, root, 1)
    print(*prices.values())


if __name__ == "__main__":
    main()
