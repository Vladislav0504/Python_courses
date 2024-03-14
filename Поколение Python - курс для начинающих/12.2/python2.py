"""Exam."""


def main():
    """My function."""
    lst_1 = list(map(int, input().split()))
    lst_2 = list(map(int, input().split()))
    lst = list(map(sum, zip(lst_1, lst_2)))
    print(*lst)


if __name__ == "__main__":
    main()
