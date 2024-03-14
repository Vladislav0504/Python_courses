"""Memory address."""


def main():
    """My function."""
    objects = [1, 2, 1, 2, 3]
    ans = len(set(map(id, objects)))
    print(ans)


if __name__ == "__main__":
    main()
