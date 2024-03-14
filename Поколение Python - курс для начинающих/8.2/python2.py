"""Exam."""


def main():
    """My function."""
    degree = 40
    count, maximum = 0, -(1 << degree)
    for _ in range(8):
        num = int(input())
        if num & 3 == 0:
            count += 1
            maximum = max(maximum, num)
    print(*(count, maximum) if count else ("NO",), sep="\n")


if __name__ == "__main__":
    main()
