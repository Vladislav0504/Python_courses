"""Conditions."""


def main():
    """My function."""
    year = int(input())
    div = (400, 4, 100)
    if year % div[0] == 0 or year % div[1] == 0 and year % div[2]:
        print("Високосный")
    else:
        print("Обычный")


if __name__ == "__main__":
    main()
