"""Files."""


def main():
    """My function."""
    with open("numbers.txt", "r", encoding="utf8") as inp:
        print(*(sum(map(int, line.split())) for line in inp), sep="\n")


if __name__ == "__main__":
    main()
