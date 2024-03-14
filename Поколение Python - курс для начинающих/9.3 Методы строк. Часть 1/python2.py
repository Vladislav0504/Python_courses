"""Strings."""


def main():
    """My function."""
    string, method = input(), "swapcase"
    print(getattr(string, method)())


if __name__ == "__main__":
    main()
