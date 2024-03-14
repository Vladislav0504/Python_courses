"""Exam."""
from typing import TypeVar

T = TypeVar("T")
V = TypeVar("V")


def merge(values: list[dict[T, V]]) -> dict[T, set[V]]:
    """Merge."""
    res = {}
    for dictionary in values:
        for key, value in dictionary.items():
            res.setdefault(key, set()).add(value)
    return res


def main():
    """My function."""
    res = merge([{"a": 1, "b": 2}, {"b": 10, "c": 100},
                 {"a": 1, "b": 17, "c": 50}, {"a": 5, "d": 777}])
    assert res == {"a": {1, 5}, "b": {2, 10, 17}, "c": {50, 100}, "d": {777}}


if __name__ == "__main__":
    main()
