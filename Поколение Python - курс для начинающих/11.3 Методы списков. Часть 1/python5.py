"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    lst = [i for i in range(1, int(num_n**0.5) + 1) if num_n % i == 0]
    start = -1 - (lst[-1]**2 == num_n)
    lst.extend([num_n // num for num in lst[start::-1]])
    print(lst)


if __name__ == "__main__":
    main()
