"""Loops."""


def main():
    """My function."""
    num_n = int(input())
    for i in range(1, num_n + 1):
        counter = 0
        for j in range(1, int(i**0.5) + 1):
            if j**2 == i:
                counter += 1
            elif i % j == 0:
                counter += 2
        print(i, "+" * counter, sep="")


if __name__ == "__main__":
    main()
