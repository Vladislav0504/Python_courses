"""Functions."""


def matrix(size_1: int = 1, size_2: int = None,
           value: int = 0) -> list[list[int]]:
    """Matrix."""
    size_2 = size_2 or size_1
    return [[value] * size_2 for _ in range(size_1)]


def main():
    """My function."""
    assert matrix() == [[0]]
    assert matrix(3) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert matrix(2, 5) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert matrix(3, 4, 9) == [[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]


if __name__ == "__main__":
    main()
