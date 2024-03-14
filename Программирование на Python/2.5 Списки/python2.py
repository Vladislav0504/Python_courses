"""Lists."""


def main():
    """My function."""
    lst = tuple(map(int, input().split()))
    if len(lst) == 1:
        print(lst[0])
    else:
        print(*map(sum, zip(lst[-1:] + lst[:], lst[1:] + lst[:1])), sep=" ")


if __name__ == "__main__":
    main()
