"""Files."""


def main():
    """My function."""
    with open("text.txt", "r", encoding="utf8") as inp:
        print(inp.read()[::-1])


if __name__ == "__main__":
    main()
