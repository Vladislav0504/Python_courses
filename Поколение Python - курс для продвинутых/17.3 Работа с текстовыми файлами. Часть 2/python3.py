"""Files."""


def main():
    """My function."""
    with open("lines.txt", "r", encoding="utf8") as inp:
        maximum = max(map(len, inp))
        inp.seek(0)
        print(*filter(lambda x: len(x) == maximum, inp), sep="")


if __name__ == "__main__":
    main()
