"""Contest."""


def main():
    """My function."""
    with open("input.txt", encoding="utf8") as inp:
        words = set(inp.read().strip().split())
        mean = sum(map(len, words)) / len(words)
        result = (word for word in words if len(word) > mean)
        print(*sorted(result, key=lambda x: (len(x), x)), sep=", ")


if __name__ == "__main__":
    main()
