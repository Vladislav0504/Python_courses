"""Exam."""


def main():
    """My function."""
    string, num_n = input().split(), int(input())
    print([string[i::num_n] for i in range(num_n)])


if __name__ == "__main__":
    main()
