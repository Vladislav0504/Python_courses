"""Lists."""


def pascal(num_n: int) -> list[int]:
    """Pascal string."""
    result = [1] * (num_n + 1)
    for i in range(1, (num_n >> 1) + 1):
        result[i] = result[i - 1] * (num_n - i + 1) // i
    for j in range((num_n >> 1) + 1, num_n):
        result[j] = result[num_n - j]
    return result


def main():
    """My function."""
    num_n = int(input())
    print(pascal(num_n))


if __name__ == "__main__":
    main()
