"""Files."""
from datetime import datetime


def main():
    """My function."""
    limit_seconds = 3600
    with open("logfile.txt", "r", encoding="utf8") as inp:
        with open("output.txt", "w", encoding="utf8") as out:
            for line in inp:
                name, time_1, time_2 = line.rstrip().split(", ")
                time_1 = datetime.strptime(time_1, "%H:%M")
                time_2 = datetime.strptime(time_2, "%H:%M")
                if (time_2 - time_1).seconds >= limit_seconds:
                    out.write(f"{name}\n")


if __name__ == "__main__":
    main()
