"""Loops."""


def main():
    """My function."""
    num_n, end = int(input()), 10
    for i in range(1, end + 1):
        result = num_n * i
        print(f"{num_n} x {i} = {result}")


if __name__ == "__main__":
    main()
