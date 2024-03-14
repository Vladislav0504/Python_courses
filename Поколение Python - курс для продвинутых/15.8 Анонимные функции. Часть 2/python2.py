"""Functions."""
from typing import Callable


def main() -> Callable[[str], bool]:
    """My function."""
    return lambda x: "a" == x[0].lower() == x[-1].lower()


if __name__ == "__main__":
    func = main()
    assert not func("abcd")
    assert not func("bcda")
    assert func("abcda")
    assert not func("Abcd")
    assert not func("bcdA")
    assert func("abcdA")
