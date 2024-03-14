"""Types."""


def main():
    """My function."""
    lst = sorted((int(input()) for _ in range(3)), reverse=True)
    print(*lst, sep="\n")


if __name__ == "__main__":
    main()
