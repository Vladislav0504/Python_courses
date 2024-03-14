"""Lists."""


def main():
    """My function."""
    num_n = int(input()[1:])
    print(*(input().split("#")[0].rstrip() for _ in range(num_n)), sep="\n")


if __name__ == "__main__":
    main()
