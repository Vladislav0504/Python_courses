"""Int function."""


def main():
    """My function."""
    num = map(int, input())
    num_1, num_2, num_3 = num
    print(num_1, num_2, num_3, sep="")
    print(num_1, num_3, num_2, sep="")
    print(num_2, num_1, num_3, sep="")
    print(num_2, num_3, num_1, sep="")
    print(num_3, num_1, num_2, sep="")
    print(num_3, num_2, num_1, sep="")


if __name__ == "__main__":
    main()
