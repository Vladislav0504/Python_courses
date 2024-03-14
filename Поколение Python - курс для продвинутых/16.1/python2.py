"""Exam."""
from typing import TypeVar

T = TypeVar("T")


def pretty_print(data: list[T], side: str = "-", delimiter: str = "|") -> None:
    """Pretty print."""
    string = f" {delimiter} ".join(map(str, ("", *data, ""))).strip()
    line = side * (len(string) - 2)
    print(f" {line}", string, f" {line}", sep="\n")


def main():
    """My function."""
    pretty_print([1, 2, 10, 23, 123, 3000])
    pretty_print(["abc", "def", "ghi", "12345"])
    pretty_print(["abc", "def", "ghi"], side="*")
    pretty_print(["abc", "def", "ghi"], delimiter="#")
    pretty_print(["abc", "def", "ghi"], side="*", delimiter="#")

    #  ------------------------------
    # | 1 | 2 | 10 | 23 | 123 | 3000 |
    #  ------------------------------
    #  -------------------------
    # | abc | def | ghi | 12345 |
    #  -------------------------
    #  *****************
    # | abc | def | ghi |
    #  *****************
    #  -----------------
    # # abc # def # ghi #
    #  -----------------
    #  *****************
    # # abc # def # ghi #
    #  *****************


if __name__ == "__main__":
    main()
