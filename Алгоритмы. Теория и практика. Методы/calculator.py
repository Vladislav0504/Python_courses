"""Dynamic programming."""


def calculator(num_n: int) -> (int, list[int]):
    """+1, *2, *3 calculator."""
    prev, count = [0] * (num_n + 1), list(range(-1, num_n))
    if num_n >= 2:
        prev[2] = 1
    for i in range(1, num_n):
        value = count[i] + 1
        for num in (i + 1, i << 1, i * 3):
            if num <= num_n and count[num] > value:
                count[num] = value
                prev[num] = i
    lst = [0] * (count[num_n] + 1)
    lst[-1] = num_n
    for k in range(count[num_n], 0, -1):
        lst[k - 1] = prev[lst[k]]
    return count[num_n], lst


def main():
    """My function."""
    num_n = int(input())
    k, lst = calculator(num_n)
    print(k)
    print(*lst)


if __name__ == "__main__":
    main()
