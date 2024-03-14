"""Files."""
from random import choice


def main():
    """My function."""
    with open("first_names.txt", "r", encoding="utf8") as file_1:
        first = file_1.read().split()
        with open("last_names.txt", "r", encoding="utf8") as file_2:
            last = file_2.read().split()
            result = tuple((choice(first), choice(last)) for _ in range(3))
            print(*(f"{f} {l}" for f, l in result), sep="\n")


if __name__ == "__main__":
    main()
