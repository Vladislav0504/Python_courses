"""Exam."""
from sys import stdin, stdout


def main():
    """My function."""
    reader = (line.strip() for line in stdin)
    num_n = int(next(reader))
    files, operations = {}, {"write": "W", "read": "R", "execute": "X"}
    for _ in range(num_n):
        file, *file_operations = next(reader).split()
        files[file] = set(file_operations)
    next(reader)
    for line in reader:
        operation, file = line.split()
        stdout.write("OK\n" if operations[operation] in files[file]
                     else "Access denied\n")


if __name__ == "__main__":
    main()
