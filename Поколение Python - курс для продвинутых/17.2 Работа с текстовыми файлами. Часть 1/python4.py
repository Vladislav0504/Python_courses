"""Files."""


def main():
    """My function."""
    with open("numbers.txt", "r", encoding="utf8") as inp:
        print(sum(map(int, inp)))


if __name__ == "__main__":
    main()
