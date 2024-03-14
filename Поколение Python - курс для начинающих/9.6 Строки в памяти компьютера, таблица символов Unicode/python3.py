"""Strings."""


def main():
    """My function."""
    num_n, string, k = int(input()), input(), 26
    print(*(chr(ord("a") + (ord(c) - ord("a") - num_n) % k) for c in string),
          sep="")


if __name__ == "__main__":
    main()
