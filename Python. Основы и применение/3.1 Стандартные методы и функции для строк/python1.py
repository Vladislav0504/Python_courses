"""Strings."""


def main():
    """My function."""
    string_s, string_a, string_b = input(), input(), input()
    k, max_operation_number = 0, 1000
    while k <= max_operation_number and string_a in string_s:
        string_s = string_s.replace(string_a, string_b)
        k += 1
    print(k if k <= max_operation_number else "Impossible")


if __name__ == "__main__":
    main()
