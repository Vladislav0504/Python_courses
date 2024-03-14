"""Exam."""


def main():
    """My function."""
    limit = 65
    with open("grades.txt", "r", encoding="utf8") as inp:
        print(sum(all(int(grade) >= limit for grade in line.split()[1:])
                  for line in inp))


if __name__ == "__main__":
    main()
