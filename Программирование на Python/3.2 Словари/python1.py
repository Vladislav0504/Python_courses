"""Dictionaries."""


def update_dictionary(dict_: dict[int, list[int]], k: int, val: int) -> None:
    """Update dictionary."""
    if k not in dict_:
        k <<= 1
    dict_.setdefault(k, []).append(val)


def main():
    """My function."""
    dictionary = {}
    assert update_dictionary(dictionary, 1, -1) is None
    assert dictionary == {2: [-1]}
    update_dictionary(dictionary, 2, -2)
    assert dictionary == {2: [-1, -2]}
    update_dictionary(dictionary, 1, -3)
    assert dictionary == {2: [-1, -2, -3]}


if __name__ == "__main__":
    main()
