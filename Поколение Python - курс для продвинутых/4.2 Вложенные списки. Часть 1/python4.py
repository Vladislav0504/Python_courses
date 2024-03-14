"""Lists."""


def main():
    """My function."""
    list_1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103],
              [1, 2, 3]]
    for elem in list_1:
        elem.reverse()
    print(list_1)


if __name__ == "__main__":
    main()
