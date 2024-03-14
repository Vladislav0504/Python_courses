"""Exam."""


def main():
    """My function."""
    with open("ledger.txt", "r", encoding="utf8") as inp:
        total = sum(int(line[1:]) for line in inp)
        print(f"${total}")


if __name__ == "__main__":
    main()
