"""Functions."""


def modify_list(lst: list[int]) -> None:
    """Modify list."""
    lst[:] = [elem >> 1 for elem in lst if not elem & 1]


def main():
    """My function."""
    lst = [1, 2, 3, 4, 5, 6]
    assert modify_list(lst) is None
    assert lst == [1, 2, 3]
    modify_list(lst)
    assert lst == [1]
    lst = [10, 5, 8, 3]
    modify_list(lst)
    assert lst == [5, 4]


if __name__ == "__main__":
    main()
