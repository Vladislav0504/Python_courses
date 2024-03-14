"""Strings."""


def main():
    """My function."""
    string_s, string_t = input(), input()
    k, i = 0, string_s.find(string_t)
    while i != -1:
        k += 1
        i = string_s.find(string_t, i + 1)
    print(k)


if __name__ == "__main__":
    main()
