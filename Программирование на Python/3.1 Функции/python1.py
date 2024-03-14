"""Functions."""


def func_f(num_x: float) -> float:
    """f(x)."""
    if num_x <= -2:
        return 1 - (num_x + 2)**2
    if -2 < num_x <= 2:
        return -num_x / 2
    return (num_x - 2)**2 + 1


def main():
    """My function."""
    assert func_f(4.5) == 7.25
    assert func_f(-4.5) == -5.25
    assert func_f(1) == -0.5


if __name__ == "__main__":
    main()
