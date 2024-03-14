"""Excel files."""
from xlrd import open_workbook


def main():
    """My function."""
    workbook = open_workbook("tab.xlsx")
    sheet_names = workbook.sheet_names()
    sheet = workbook.sheet_by_name(sheet_names[0])
    start, end = 6, 26
    print(min(sheet.row_values(row)[2] for row in range(start, end + 1)))


if __name__ == "__main__":
    main()
