"""Contest."""
from re import search


def main():
    """My function."""
    str_a, str_b = input(), input()
    pattern = ".*".join(str_a)
    print("YES" if search(pattern, str_b) and str_a != str_b else "NO")


if __name__ == "__main__":
    main()
