"""Files."""


def main():
    """My function."""
    with open("prices.txt", "r", encoding="utf8") as inp:
        reader = (map(int, line.split()[1:]) for line in inp)
        print(sum(map(lambda data: next(data) * next(data), reader)))


if __name__ == "__main__":
    main()
