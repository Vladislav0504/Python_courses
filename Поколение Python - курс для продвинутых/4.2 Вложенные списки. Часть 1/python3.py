"""Lists."""


def main():
    """My function."""
    list_1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103],
              [1, 2, 3]]
    maximum = max(max(lst) for lst in list_1)
    print(maximum)


if __name__ == "__main__":
    main()
