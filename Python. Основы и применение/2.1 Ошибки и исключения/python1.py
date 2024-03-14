"""Errors and exceptions."""


def foo_() -> None:
    """Foo."""
    print()


def main():
    """My function."""
    try:
        foo_()
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ArithmeticError:
        print("ArithmeticError")
    except AssertionError:
        print("AssertionError")


if __name__ == "__main__":
    main()
