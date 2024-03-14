"""Lists."""


def main():
    """My function."""
    print(*(int(i)**2 for i in input().split() if i[-1] in "046"))


if __name__ == "__main__":
    main()
