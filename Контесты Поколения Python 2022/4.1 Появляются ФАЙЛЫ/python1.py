"""Contest."""


def index_of_nearest(lst: list[int], num: int) -> int:
    """Index of nearest."""
    value = min(lst, key=lambda x: abs(num - x), default=-1)
    return lst.index(value) if lst else -1


def main():
    """My function."""
    assert index_of_nearest([], 17) == -1
    assert index_of_nearest([7, 13, 3, 5, 18], 0) == 2
    assert index_of_nearest([9, 5, 3, 2, 11], 4) == 1
    assert index_of_nearest([7, 5, 4, 4, 3], 4) == 2


if __name__ == "__main__":
    main()
