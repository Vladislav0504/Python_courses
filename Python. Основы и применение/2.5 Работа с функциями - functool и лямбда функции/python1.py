"""Functions."""
from typing import Callable


def mod_checker(num_x: int, mod: int = 0) -> Callable[[int], bool]:
    """Mod checker."""
    return lambda num_y: num_y % num_x == mod


def main():
    """My function."""
    mod_3 = mod_checker(3)

    print(mod_3(3))  # True
    print(mod_3(4))  # False

    mod_3_1 = mod_checker(3, 1)
    print(mod_3_1(4))  # True


if __name__ == "__main__":
    main()
