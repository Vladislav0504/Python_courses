"""Sets."""


def main():
    """My function."""
    string_1, string_2 = input(), input()
    my_set = set(string_1).union(set(string_2))
    print("YES" if len(my_set) == 10 else "NO")


if __name__ == "__main__":
    main()
