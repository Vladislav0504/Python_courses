"""Files."""
from random import choice


def main():
    """My function."""
    with open("lines.txt", "r", encoding="utf8") as inp:
        print(choice(inp.readlines()))


if __name__ == "__main__":
    main()
