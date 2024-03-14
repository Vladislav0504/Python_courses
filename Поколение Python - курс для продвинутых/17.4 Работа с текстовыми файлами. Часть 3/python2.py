"""Files."""
from random import randint


def main():
    """My function."""
    with open("random.txt", "w", encoding="utf8") as out:
        interval, k = (111, 777), 25
        print(*(randint(*interval) for _ in range(k)), sep="\n", file=out)


if __name__ == "__main__":
    main()
