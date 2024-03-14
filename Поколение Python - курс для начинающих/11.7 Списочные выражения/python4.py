"""Lists."""


def main():
    """My function."""
    k = (100, 1000)
    palindromes = [i for i in range(k[0], k[1] + 1) if str(i) == str(i)[::-1]]
    print(palindromes)


if __name__ == "__main__":
    main()
