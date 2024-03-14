"""Contest."""


def main():
    """My function."""
    numbers, num_n = set(), input()
    while num_n not in numbers:
        numbers.add(num_n)
        num_n = str(sum(int(i)**2 for i in num_n))
        if int(num_n) == 1:
            print("YES")
            break
    else:
        print("NO")


if __name__ == "__main__":
    main()
