"""Lists."""


def main():
    """My function."""
    lst, result = input().split(), [[]]
    for step in range(1, len(lst) + 1):
        result.extend([lst[i:i + step] for i in range(len(lst) - step + 1)])
    print(result)


if __name__ == "__main__":
    main()
