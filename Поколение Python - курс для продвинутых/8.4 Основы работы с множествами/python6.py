"""Sets."""


def main():
    """My function."""
    string = input()
    print("NO" if len(string) - len(set(string)) else "YES")


if __name__ == "__main__":
    main()
