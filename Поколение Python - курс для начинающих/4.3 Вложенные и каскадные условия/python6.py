"""Conditions."""


def main():
    """My function."""
    n_1, n_2, string = int(input()), int(input()), input()
    act = {"+": "__add__", "-": "__sub__", "*": "__mul__", "/": "__truediv__"}
    if string not in act:
        print("Неверная операция")
    elif string == "/" and n_2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(getattr(n_1, act[string])(n_2))


if __name__ == "__main__":
    main()
