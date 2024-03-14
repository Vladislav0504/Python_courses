"""Exam."""
from typing import TypeVar

T = TypeVar("T")


def concat(*args: T, sep: str = " ") -> str:
    """Concat."""
    return sep.join(map(str, args))


def main():
    """My function."""
    assert concat("hello", "python", "and",
                  "stepik") == "hello python and stepik"
    assert concat("hello", "python", "and", "stepik",
                  sep="*") == "hello*python*and*stepik"
    assert concat("hello", "python", sep="()()()") == "hello()()()python"
    assert concat("hello", sep="()") == "hello"
    assert concat(1, 2, 3, 4, 5, 6, 7, 8, 9,
                  sep="$$") == "1$$2$$3$$4$$5$$6$$7$$8$$9"


if __name__ == "__main__":
    main()
