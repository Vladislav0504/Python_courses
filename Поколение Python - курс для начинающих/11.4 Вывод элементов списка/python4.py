"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    lst, result = [input() for _ in range(num_n)], []
    lst_set = set(lst)
    for string in lst:
        if string in lst_set:
            result.append(string)
            lst_set.remove(string)
    print(*result, sep="\n")


if __name__ == "__main__":
    main()
