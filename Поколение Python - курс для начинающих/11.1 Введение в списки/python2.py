"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    print([chr(ord("a") + i) for i in range(num_n)])


if __name__ == "__main__":
    main()
