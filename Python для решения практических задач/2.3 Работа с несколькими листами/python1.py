"""Excel files."""
from xlrd import open_workbook


def main():
    """My function."""
    workbook = open_workbook("trekking1.xlsx")
    sheet = workbook.sheet_by_index(0)  # выбор листа
    calorie = dict(zip(sheet.col_values(0)[1:], sheet.col_values(1)[1:]))
    print(*sorted(calorie, key=lambda food: (-calorie[food], food)), sep="\n")


if __name__ == "__main__":
    main()
