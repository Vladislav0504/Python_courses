"""Array. Stack. Queue."""


def main():
    """My function."""
    queue, result = 0, 0
    string = input()
    for num in map(int, string.split()):
        if num == 0:
            queue += 1
        elif queue:
            queue -= 1
        else:
            result += 1
    print(result)


if __name__ == "__main__":
    main()
