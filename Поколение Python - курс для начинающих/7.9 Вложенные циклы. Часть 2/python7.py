"""Loops."""


def main():
    """My function."""
    num_a, num_b = int(input()), int(input())
    for i in range(max(num_a, 2), num_b + 1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)


if __name__ == "__main__":
    main()
