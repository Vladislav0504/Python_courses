"""Int function."""


def main():
    """My function."""
    num = int(input())
    prev_num = num - 1
    next_num = num + 1
    print(f"Следующее за числом {num} число: {next_num}")
    print(f"Для числа {num} предыдущее число: {prev_num}")


if __name__ == "__main__":
    main()
