"""Conditions."""


def main():
    """My function."""
    num_1, num_2, num_3, num_4 = map(int, input())
    if num_1 + num_4 == num_2 - num_3:
        print("ДА")
    else:
        print("НЕТ")


if __name__ == "__main__":
    main()
