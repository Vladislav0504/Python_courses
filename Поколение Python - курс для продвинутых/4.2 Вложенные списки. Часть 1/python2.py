"""Lists."""


def main():
    """My function."""
    list_1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sub_list = ["h", "i", "j"]
    list_1[2][1][2].extend(sub_list)
    print(list_1)


if __name__ == "__main__":
    main()
