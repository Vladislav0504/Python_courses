"""Functions."""


def find_all(target: str, symbol: str) -> list[int]:
    """List of symbol indexes in target."""
    result, index = [], target.find(symbol)
    while index != -1:
        result.append(index)
        index = target.find(symbol, index + 1)
    return result


def main():
    """My function."""
    string, char = input(), input()
    print(find_all(string, char))


if __name__ == "__main__":
    main()
