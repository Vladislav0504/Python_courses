"""Contest."""


def main():
    """My function."""
    russian = "АаВСсЕеНКМОоРрТХху"
    chars = (input() for _ in range(3))
    count = sum(char in russian for char in chars)
    if count == 3:
        print("ru")
    elif count == 0:
        print("en")
    else:
        print("mix")


if __name__ == "__main__":
    main()
