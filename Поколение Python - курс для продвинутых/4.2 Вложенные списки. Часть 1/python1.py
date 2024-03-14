"""Lists."""


def main():
    """My function."""
    numb = 7000
    list_1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    list_1[2][2].append(numb)
    print(list_1)


if __name__ == "__main__":
    main()
