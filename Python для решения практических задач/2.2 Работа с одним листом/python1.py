"""Excel files."""
from xlrd import open_workbook


def main():
    """My function."""
    workbook = open_workbook("salaries.xlsx")
    sheet = workbook.sheet_by_index(0)  # выбор листа
    by_region = {k: sorted(sheet.row_values(i)[1:])
                 for i, k in enumerate(sheet.col_values(0)[1:], 1)}
    for region, salaries in by_region.items():
        index = len(salaries) >> 1
        if len(salaries) & 1:
            by_region[region] = salaries[index]
        else:
            by_region[region] = sum(salaries[index - 1:index + 1]) / 2
    by_profession = {k: sum(sheet.col_values(i)[1:])
                     for i, k in enumerate(sheet.row_values(0)[1:], 1)}
    answer = []
    for dictionary in (by_region, by_profession):
        answer.append(max(dictionary.items(), key=lambda pair: pair[1])[0])
    print(*answer)


if __name__ == "__main__":
    main()
