"""Problems."""


def main():
    """My function."""
    grades = 11
    results = tuple([0, 0] for _ in range(grades))
    with open("dataset_3380_5.txt", "r", encoding="utf8") as file:
        for line in file:
            grade, _, height = line.split()
            results[int(grade) - 1][0] += int(height)
            results[int(grade) - 1][1] += 1
    with open("text5.txt", "w", encoding="utf8") as file:
        for i, (total, count) in enumerate(results, 1):
            if not count:
                mean = "-"
            else:
                mean = total / count
            file.write(f"{i} {mean}\n")


if __name__ == "__main__":
    main()
