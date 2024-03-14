"""Types."""


def main():
    """My function."""
    cities = [input() for _ in range(3)]
    print(min(cities, key=len), max(cities, key=len), sep="\n")


if __name__ == "__main__":
    main()
