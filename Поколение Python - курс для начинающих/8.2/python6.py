"""Exam."""


def main():
    """My function."""
    num, digits = input(), [0] * 10
    for k in map(int, num):
        digits[k] += 1
    count_3, count_last = digits[3], digits[int(num[-1])]
    count_even, count_0_5 = sum(digits[::2]), digits[0] + digits[5]
    total_more_5 = sum(i * digits[i] for i in range(6, 10))
    prod_more_7 = 1
    for digit in (8, 9):
        prod_more_7 *= digit**digits[digit]
    print(count_3, count_last, count_even, sep="\n")
    print(total_more_5, prod_more_7, count_0_5, sep="\n")


if __name__ == "__main__":
    main()
