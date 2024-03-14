"""Conditions."""


def main():
    """My function."""
    year, div = int(input()), (400, 4, 100)
    if year % div[0] == 0 or year % div[1] == 0 and year % div[2]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
