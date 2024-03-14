"""Files."""
from re import findall


def main():
    """My function."""
    with open("nums.txt", "r", encoding="utf8") as inp:
        print(sum(sum(map(int, findall(r"\d+", line))) for line in inp))


if __name__ == "__main__":
    main()
