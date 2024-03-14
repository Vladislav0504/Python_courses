"""Problems."""


def main():
    """My function."""
    lst = map(int, input().split())
    num_x = int(input())
    lst = " ".join(str(i) for i, k in enumerate(lst) if k == num_x)
    print(lst or "Отсутствует")


if __name__ == "__main__":
    main()
