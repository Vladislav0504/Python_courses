"""Lists."""


def chunked(lst: list[str], num_n: int) -> list[list[str]]:
    """Chunked list."""
    return [lst[i:i + num_n] for i in range(0, len(lst), num_n)]


def main():
    """My function."""
    string, num_n = input().split(), int(input())
    print(chunked(string, num_n))


if __name__ == "__main__":
    main()
