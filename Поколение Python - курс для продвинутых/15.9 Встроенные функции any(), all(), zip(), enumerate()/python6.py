"""Functions."""


def main():
    """My function."""
    password = input()
    cond_1 = any(map(str.isdigit, password))
    cond_2 = any(map(str.isupper, password))
    cond_3 = any(map(str.islower, password))
    print("YES" if all((len(password) >= 7, cond_1, cond_2, cond_3)) else "NO")


if __name__ == "__main__":
    main()
