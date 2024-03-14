"""Conditions."""


def main():
    """My function."""
    a_1, b_1, a_2, b_2 = (int(input()) for _ in range(4))
    if a_2 < a_1:
        a_1, b_1, a_2, b_2 = a_2, b_2, a_1, b_1
    if a_2 > b_1:
        print("пустое множество")
    elif a_2 == b_1:
        print(a_2)
    else:
        print(a_2, min(b_1, b_2))


if __name__ == "__main__":
    main()
