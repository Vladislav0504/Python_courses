"""CSV format."""
import csv


def main():
    """My function."""
    with open("Crimes.csv", "r", encoding="utf8") as file:
        reader = csv.reader(file)
        columns, crimes = next(reader), {}
        date = columns.index("Date")
        primary_type = columns.index("Primary Type")
        for line in reader:
            if "2015" in line[date]:
                crime = line[primary_type]
                crimes[crime] = crimes.get(crime, 0) + 1
    print(max(crimes.items(), key=lambda pair: pair[1])[0])


if __name__ == "__main__":
    main()
