"""Functions."""
from math import sin


def main():
    """My function."""
    k, func = int(input()), input()
    functions = {"квадрат": lambda x: x**2, "куб": lambda x: x**3,
                 "корень": lambda x: x**0.5, "модуль": abs, "синус": sin}
    print(functions[func](k))


if __name__ == "__main__":
    main()
