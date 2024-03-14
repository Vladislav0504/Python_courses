"""Int function."""


def main():
    """My function."""
    n_students = int(input())
    k_tangerine = int(input())
    print(*divmod(k_tangerine, n_students), sep="\n")


if __name__ == "__main__":
    main()
