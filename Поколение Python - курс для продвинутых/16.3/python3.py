"""Exam."""


def main():
    """My function."""
    words = "the world is mine take a look what you have started".split()
    print(*map(lambda w: f"\"{w}\"", words))


if __name__ == "__main__":
    main()
