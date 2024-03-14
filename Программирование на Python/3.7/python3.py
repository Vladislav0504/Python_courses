"""Problems."""


def main():
    """My function."""
    num_d = int(input())
    words = {input().lower() for _ in range(num_d)}
    mistakes, num_l = set(), int(input())
    for _ in range(num_l):
        mistakes |= {w for w in input().lower().split() if w not in words}
    print(*mistakes, sep="\n")


if __name__ == "__main__":
    main()
