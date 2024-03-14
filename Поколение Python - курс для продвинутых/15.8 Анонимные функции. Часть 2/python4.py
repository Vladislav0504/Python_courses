"""Functions."""
from typing import Callable


def main() -> Callable[[str], bool]:
    """My function."""
    return lambda x: (x[0].strip("-") + x[1:]).replace(".", "", 1).isdigit()


if __name__ == "__main__":
    is_num = main()
    assert not is_num("10.34ab")
    assert is_num("10.45")
    assert is_num("-18")
    assert is_num("-34.67")
    assert is_num("987")
    assert not is_num("abcd")
    assert not is_num("123.122.12")
    assert is_num("-123.122")
    assert not is_num("--13.2")
