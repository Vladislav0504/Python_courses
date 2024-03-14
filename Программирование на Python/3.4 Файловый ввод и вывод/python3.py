"""Files."""


def main():
    """My function."""
    count, marks = 0, [0, 0, 0]
    with open("dataset_3363_4.txt", "r", encoding="utf8") as inp:
        with open("text3.txt", "w", encoding="utf8") as out:
            for line in inp:
                mean, grades = 0, map(int, line.split(";")[1:])
                for i, grade in enumerate(grades):
                    marks[i] += grade
                    mean += grade
                mean /= 3
                out.write(f"{mean}\n")
                count += 1
            for j in range(3):
                marks[j] /= count
            out.write("{} {} {}".format(*marks))


if __name__ == "__main__":
    main()
