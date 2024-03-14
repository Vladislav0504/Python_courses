"""Dictionaries."""


def main() -> dict[int, list[int]]:
    """My function."""
    numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6,
               87, 1000, 13456, 360]
    res = {}
    for k in numbers:
        lst = [i for i in range(1, int(k**0.5) + 1) if k % i == 0]
        lst.extend([k // num for num in lst[-1 - ((lst[-1])**2 == k)::-1]])
        res[k] = lst
    return res


if __name__ == "__main__":
    result = main()
    print(result)
