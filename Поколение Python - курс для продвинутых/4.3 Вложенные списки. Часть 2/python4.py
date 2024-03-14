"""Lists."""


def pascal(num_n: int) -> None:
    """Pascal's triangle."""
    lst_1 = []
    for k in range(num_n):
        lst_1.append(1)
        lst_2 = lst_1.copy()
        for i in range(1, (k >> 1) + 1):
            lst_2[i] += lst_1[i - 1]
        for j in range((k >> 1) + 1, k):
            lst_2[j] = lst_2[k - j]
        print(*lst_2)
        lst_1 = lst_2


def main():
    """My function."""
    num_n = int(input())
    pascal(num_n)


if __name__ == "__main__":
    main()
