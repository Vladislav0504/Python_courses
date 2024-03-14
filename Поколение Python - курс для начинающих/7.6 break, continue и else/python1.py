"""Loops."""


def main():
    """My function."""
    num_n = int(input())
    for i in range(2, int(num_n**0.5) + 1):
        if num_n % i == 0:
            print(i)
            break
    else:
        print(num_n)


if __name__ == "__main__":
    main()
