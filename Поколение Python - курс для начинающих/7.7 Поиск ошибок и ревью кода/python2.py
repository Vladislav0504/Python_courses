"""Loops."""


def main():
    """My function."""
    max_neg, total_neg = -10**6, 0
    for _ in range(10):
        num = int(input())
        if num < 0:
            total_neg += num
            max_neg = max(num, max_neg)
    print(*(total_neg, max_neg) if total_neg else ("NO",), sep="\n")


if __name__ == "__main__":
    main()
