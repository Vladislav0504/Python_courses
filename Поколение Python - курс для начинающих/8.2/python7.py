"""Exam."""


def main():
    """My function."""
    min_num, counter, limit = 0, 0, 1
    while counter < 5:
        count = 0
        min_num += 1
        if limit**3 <= (min_num >> 1):
            limit += 1
        for i in range(1, limit):
            j_3 = min_num - i**3
            j = int(j_3**(1 / 3))
            if j_3 in (j**3, (j + 1)**3):
                count += 1
            if count == 2:
                print(min_num)
                counter += 1
                break


if __name__ == "__main__":
    main()
