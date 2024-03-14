"""Lists."""


def main():
    """My function."""
    data = input().split()
    print("".join((f"{word[0]}." for word in data)))


if __name__ == "__main__":
    main()
