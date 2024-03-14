"""Excel files."""
from xlrd import open_workbook, sheet


def nutritional_value(sheet_1: sheet.Sheet) -> dict[str, (str, str, str, str)]:
    """Nutritional value."""
    products = sheet_1.col_values(0)[1:]
    calories, proteins = sheet_1.col_values(1)[1:], sheet_1.col_values(2)[1:]
    fats, carbohydrates = sheet_1.col_values(3)[1:], sheet_1.col_values(4)[1:]
    return dict(zip(products, zip(calories, proteins, fats, carbohydrates)))


def main():
    """My function."""
    workbook = open_workbook("trekking2.xlsx")
    value = nutritional_value(workbook.sheet_by_name("Справочник"))
    sheet_2 = workbook.sheet_by_name("Раскладка")
    products, masses = sheet_2.col_values(0)[1:], sheet_2.col_values(1)[1:]
    print(*(int(sum((value[product][j] or 0) * mass
                    for product, mass in zip(products, masses)) // 100)
            for j in range(4)))


if __name__ == "__main__":
    main()
