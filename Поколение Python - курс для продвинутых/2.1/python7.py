"""Repetition."""


def main():
    """My function."""
    number = input()
    start, lst = len(number) % 3, []
    if start:
        lst.append(number[:start])
    lst.extend([number[i:i + 3] for i in range(start, len(number), 3)])
    print(",".join(lst))


if __name__ == "__main__":
    main()
