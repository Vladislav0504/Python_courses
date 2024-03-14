"""Lists."""


def main():
    """My function."""
    k = 26
    print([chr(ord("a") + i) * (i + 1) for i in range(k)])


if __name__ == "__main__":
    main()
