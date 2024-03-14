"""Contest."""


def main():
    """My function."""
    num_n, emails = int(input()), {}
    for _ in range(num_n):
        employee, i = input().split("@")[0], 0
        while i < len(employee) and not employee[i].isdigit():
            i += 1
        num = int(employee[i:] or 0)
        emails.setdefault(employee[:i], set()).add(num)
    num_m = int(input())
    for _ in range(num_m):
        name, index = input(), 0
        emails.setdefault(name, set())
        while index in emails[name]:
            index += 1
        emails[name].add(index)
        print(str(index or "").join((name, "@beegeek.bzz")))


if __name__ == "__main__":
    main()
