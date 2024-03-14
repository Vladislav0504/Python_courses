"""Contest."""


def main():
    """My function."""
    num_n = int(input())
    initial = (0, 1, 1)
    for _ in range(num_n - 2):
        initial = (initial[1], initial[2], sum(initial))
    print(initial[num_n] if num_n < 3 else initial[2])


if __name__ == "__main__":
    main()
