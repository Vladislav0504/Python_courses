"""Functions."""
from typing import Callable


def main() -> Callable[[int], bool]:
    """My function."""
    dividers = (19, 13)
    return lambda x: 0 in (x % dividers[0], x % dividers[1])


if __name__ == "__main__":
    func = main()
    assert func(19)
    assert func(13)
    assert not func(20)
    assert not func(15)
    assert func(247)
