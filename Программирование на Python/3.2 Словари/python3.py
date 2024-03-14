"""Dictionaries."""


def func_f(num_x: float) -> float:
    """f(x)."""
    return -num_x / 2


def main():
    """My function."""
    num_n, dictionary = int(input()), {}
    for _ in range(num_n):
        num_x = int(input())
        if num_x not in dictionary:
            dictionary[num_x] = func_f(num_x)
        print(dictionary[num_x])


if __name__ == "__main__":
    main()
