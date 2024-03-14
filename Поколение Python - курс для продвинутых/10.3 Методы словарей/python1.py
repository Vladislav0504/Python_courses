"""Dictionaries."""


def main() -> dict[int, int]:
    """My function."""
    start, end = 1, 15
    return {i: i**2 for i in range(start, end + 1)}


if __name__ == "__main__":
    result = main()
    print(result)
