"""Dynamic programming."""


def min_max(table: list[list[(int, int)]], string: str, i: int,
            j: int) -> (int, int):
    """Minimum, maximum."""
    operation = {"+": lambda x, y: x + y,
                 "-": lambda x, y: x - y,
                 "*": lambda x, y: x * y}
    actions = tuple(operation[char] for char in string[1::2])
    degree = 50
    minimum, maximum = 1 << degree, -(1 << degree)
    for k in range(i, j):
        for num_1 in table[i][k]:
            for num_2 in table[k + 1][j]:
                res = actions[k](num_1, num_2)
                minimum = min(minimum, res)
                maximum = max(maximum, res)
    return minimum, maximum


def max_brackets(string: str) -> int:
    """Best bracket locality."""
    size = (len(string) >> 1) + 1
    table = [[(0,)] * size for _ in range(size)]
    for i, char in enumerate(string[::2]):
        table[i][i] = (int(char),)
    for k in range(1, size):
        for j in range(k, size):
            table[j - k][j] = min_max(table, string, j - k, j)
    return max(table[0][-1])


def main():
    """My function."""
    string = input()
    print(max_brackets(string))


if __name__ == "__main__":
    main()
