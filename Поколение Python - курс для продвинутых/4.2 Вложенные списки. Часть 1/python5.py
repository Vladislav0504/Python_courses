"""Lists."""


def main():
    """My function."""
    list_1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103],
              [1, 2, 3]]
    total, counter = sum(map(sum, list_1)), sum(map(len, list_1))
    print(total / counter)


if __name__ == "__main__":
    main()
