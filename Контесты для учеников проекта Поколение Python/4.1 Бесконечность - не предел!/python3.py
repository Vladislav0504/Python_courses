"""Contest."""


def main():
    """My function."""
    num_n, i = int(input()), 1
    while num_n > len(str(i)):
        num_n -= len(str(i))
        i += 1
    print(str(i)[num_n - 1])


if __name__ == "__main__":
    main()
