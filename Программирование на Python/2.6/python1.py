"""Problems."""


def main():
    """My function."""
    num = int(input())
    total, total_2 = num, num**2
    while total:
        num = int(input())
        total += num
        total_2 += num**2
    print(total_2)


if __name__ == "__main__":
    main()
