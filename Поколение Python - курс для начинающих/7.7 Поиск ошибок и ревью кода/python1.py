"""Loops."""


def main():
    """My function."""
    count, prod = 0, 1
    for _ in range(10):
        num = int(input())
        if num >= 0:
            prod *= num
            count += 1
    print(*(count, prod) if count else ("NO",), sep="\n")


if __name__ == "__main__":
    main()
