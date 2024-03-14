"""Files."""


def main():
    """My function."""
    with open("input.txt", "r", encoding="utf8") as inp:
        with open("output.txt", "w", encoding="utf8") as out:
            print(*(f"{i}) {line}" for i, line in enumerate(inp, 1)), sep="",
                  file=out)


if __name__ == "__main__":
    main()
