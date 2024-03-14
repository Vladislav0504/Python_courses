"""Loops."""


def main():
    """My function."""
    num_n = int(input())
    for i in range(1, num_n + 1):
        for j in range(1, 10):
            result = i + j
            print(f"{i} + {j} = {result}")
        print()


if __name__ == "__main__":
    main()
