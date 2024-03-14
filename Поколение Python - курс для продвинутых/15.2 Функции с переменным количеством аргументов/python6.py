"""Functions."""
from typing import TypeVar

T = TypeVar("T")


def info_kwargs(**kwargs: T) -> None:
    """Print info kwargs."""
    print(*(f"{name}: {kwargs[name]}" for name in sorted(kwargs)), sep="\n")


def main():
    """My function."""
    info_kwargs(first_name="Timur", last_name="Guev", age=28, job="teacher")
    # age: 28
    # first_name: Timur
    # job: teacher
    # last_name: Guev


if __name__ == "__main__":
    main()
