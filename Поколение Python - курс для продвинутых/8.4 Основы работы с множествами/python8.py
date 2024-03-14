"""Sets."""


def main():
    """My function."""
    string_1, string_2 = input(), input()
    print("YES" if set(string_1) == set(string_2) else "NO")


if __name__ == "__main__":
    main()
