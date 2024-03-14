"""Exam."""


def main():
    """My function."""
    words = input().split()
    lst = ["".join((word[1:], word[0], "ки")) for word in words]
    print(*lst)


if __name__ == "__main__":
    main()
