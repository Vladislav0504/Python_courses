"""Dictionaries."""


def main() -> list[dict[str, dict[str, int]]]:
    """My function."""
    student_ids = ["S001", "S002", "S003", "S004", "S005", "S006", "S007",
                   "S008", "S009", "S010", "S011", "S012", "S013"]
    student_names = ["Camila Rodriguez", "Juan Cruz", "Dan Richards",
                     "Sam Boyle", "Batista Cesare", "Francesco Totti",
                     "Khalid Hussain", "Ethan Hawke", "David Bowman",
                     "James Milner", "Michael Owen", "Gary Oldman",
                     "Tom Hardy"]
    student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
    return [{student_id: {name: grade}} for student_id, name, grade in
            zip(student_ids, student_names, student_grades)]


if __name__ == "__main__":
    result = main()
    print(result)
