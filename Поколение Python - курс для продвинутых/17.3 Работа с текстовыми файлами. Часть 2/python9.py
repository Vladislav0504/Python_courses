"""Files."""


def read_csv() -> list[dict[str, str]]:
    """Read csv."""
    with open("data.csv", "r", encoding="utf8") as inp:
        reader = (line.strip().split(",") for line in inp)
        keys = next(reader)
        return [dict(zip(keys, values)) for values in reader]


def main():
    """My function."""
    print(read_csv())


if __name__ == "__main__":
    main()
