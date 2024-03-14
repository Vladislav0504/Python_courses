"""Dynamic programming."""
INF = 10**2


def edit_distance(string_1: list[str], string_2: list[str]) -> int:
    """Edit distance."""
    num_n, num_m = len(string_1), len(string_2)
    if num_m < num_n:
        num_n, num_m = num_m, num_n
        string_1, string_2 = string_2, string_1
    prev, cur = list(range(num_n + 1)), [INF] * (num_n + 1)
    for j, char_2 in enumerate(string_2, 1):
        cur[0] = j
        for i, char_1 in enumerate(string_1, 1):
            cur[i] = min(cur[i - 1] + 1, prev[i] + 1,
                         prev[i - 1] + (char_1 != char_2))
        prev, cur = cur, prev
    return prev[num_n]


def main():
    """My function."""
    string_1, string_2 = list(input()), list(input())
    print(edit_distance(string_1, string_2))


if __name__ == "__main__":
    main()
