"""Functions."""


def main():
    """My function."""
    limit = 255
    print(all(x.isdigit() and int(x) <= limit for x in input().split(".")))


if __name__ == "__main__":
    main()
