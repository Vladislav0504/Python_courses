"""Lists."""


def main():
    """My function."""
    string, result = input().split(), []
    for elem in string:
        if result and elem == result[-1][0]:
            result[-1].append(elem)
        else:
            result.append([elem])
    print(result)


if __name__ == "__main__":
    main()
