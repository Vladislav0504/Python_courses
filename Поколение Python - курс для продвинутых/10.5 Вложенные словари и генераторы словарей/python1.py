"""Dictionaries."""


def main() -> dict[int, int]:
    """My function."""
    numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19,
               1, 6, 87]
    return {i: value**2 for i, value in enumerate(numbers)}


if __name__ == "__main__":
    result = main()
    print(result)
