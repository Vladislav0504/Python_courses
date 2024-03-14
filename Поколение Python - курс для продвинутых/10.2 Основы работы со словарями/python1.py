"""Dictionaries."""


def main():
    """My function."""
    keys = [1.12, 67.9, 3.11, 7.9, 9.2, 7.1, 0.12, 1.91, 10.12, 99.0]
    values = ["aa", 45, "ccc", "dd", "ee", "ff", "qq", "aa", [1, 2, 3],
              {9, 0, 1}]
    my_dict = dict(zip(keys, values))
    print(min(my_dict) + max(my_dict))


if __name__ == "__main__":
    main()
