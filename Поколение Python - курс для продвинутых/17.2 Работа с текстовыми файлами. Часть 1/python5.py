"""Files."""


def main():
    """My function."""
    with open("nums.txt", "r", encoding="utf8") as inp:
        print(sum(map(int, inp.read().split())))


if __name__ == "__main__":
    main()
