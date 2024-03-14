"""Classes."""
from time import ctime

from typing import List, TypeVar, Generic

from sys import modules

T = TypeVar("T")
PARENT_NAME = "Loggable"


class Loggable(Generic[T]):
    """Loggable."""

    @staticmethod
    def log(message: T) -> None:
        """Log message."""
        print(ctime(), ": ", message, sep="")

    @staticmethod
    def hello() -> None:
        """Hello."""
        print("Hello!")


ClassLog = getattr(modules[__name__], PARENT_NAME)


class LoggableList(Generic[T], List, ClassLog):
    """LoggableList."""

    def __init__(self, *iterable: T) -> None:
        """Loggable list constructor."""
        super().__init__(*iterable)
        self.log_count = 0

    def append(self, elem: T) -> None:
        """Append with log."""
        super().append(elem)
        self.log(elem)
        self.log_count += 1


def main():
    """My function."""
    lst = LoggableList()
    lst.append(2)
    print(lst)
    print(lst.log_count)
    Loggable.hello()


if __name__ == "__main__":
    main()
