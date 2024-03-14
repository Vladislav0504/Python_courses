"""Contest."""


def main():
    """My function."""
    num = int(input())
    flag = "YES"
    if num == 1:
        flag = "NO"
    for i in (2, 3, 5):
        while num % i == 0:
            num //= i
    if num != 1:
        flag = "NO"
    print(flag)


if __name__ == "__main__":
    main()
