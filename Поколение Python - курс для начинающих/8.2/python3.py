"""Exam."""


def main():
    """My function."""
    count, maximum = 0, -10**8
    for _ in range(4):
        num = int(input())
        if num & 1:
            count += 1
            maximum = max(maximum, num)
    print(*(count, maximum) if count else ("NO",), sep="\n")


if __name__ == "__main__":
    main()
