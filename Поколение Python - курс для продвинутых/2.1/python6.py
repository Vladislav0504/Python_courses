"""Repetition."""


def main():
    """My function."""
    number = input()
    if len(number) == 5:
        print(int(number[::-1]))
    else:
        print(number[0] + number[1:][::-1])


if __name__ == "__main__":
    main()
