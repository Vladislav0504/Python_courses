"""Files."""


def main():
    """My function."""
    with open("data.txt", "r", encoding="utf8") as inp:
        print(*inp.readlines()[::-1], sep="")


if __name__ == "__main__":
    main()
