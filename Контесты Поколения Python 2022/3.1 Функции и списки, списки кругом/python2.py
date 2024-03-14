"""Contest."""


def main():
    """My function."""
    num_n, languages = int(input()), set()
    if num_n:
        languages = set(input().split(", "))
    for _ in range(num_n - 1):
        languages &= set(input().split(", "))
    print(*sorted(languages) if languages else ("Сериал снять не удастся",),
          sep=", ")


if __name__ == "__main__":
    main()
