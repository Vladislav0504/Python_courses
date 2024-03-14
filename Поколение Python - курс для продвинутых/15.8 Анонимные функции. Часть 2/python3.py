"""Functions."""
from typing import Callable


def main() -> Callable[[str], bool]:
    """My function."""
    return lambda x: x.replace(".", "", 1).isdigit()


if __name__ == "__main__":
    is_non_negative_num = main()
    assert not is_non_negative_num("10.34ab")
    assert is_non_negative_num("10.45")
    assert not is_non_negative_num("-18")
    assert not is_non_negative_num("-34.67")
    assert is_non_negative_num("987")
    assert not is_non_negative_num("abcd")
    assert not is_non_negative_num("123.122.12")
    assert is_non_negative_num("123.122")
