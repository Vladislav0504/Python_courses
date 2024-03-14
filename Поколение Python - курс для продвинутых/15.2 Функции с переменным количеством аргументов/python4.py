"""Functions."""


def greet(first: str, *names: str) -> str:
    """Greet."""
    string = " and ".join((first, *names))
    return f"Hello, {string}!"


def main():
    """My function."""
    assert greet("Timur") == "Hello, Timur!"
    assert greet("Timur", "Roman") == "Hello, Timur and Roman!"
    assert greet("Timur", "Roman",
                 "Ruslan") == "Hello, Timur and Roman and Ruslan!"


if __name__ == "__main__":
    main()
