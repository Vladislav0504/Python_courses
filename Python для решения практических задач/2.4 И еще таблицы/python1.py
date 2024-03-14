"""Excel files."""
from urllib.request import urlretrieve

from zipfile import ZipFile

from xlrd import open_workbook


def main():
    """My function."""
    url = "https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip"
    local_filename, _ = urlretrieve(url)
    lst = []
    with ZipFile(local_filename, "r") as zip_ref:
        for file in zip_ref.namelist():
            workbook = open_workbook(file_contents=zip_ref.read(file))
            sheet = workbook.sheet_by_index(0)
            lst.append((sheet.row_values(1)[1], int(sheet.row_values(1)[3])))
    print(*(f"{name} {salary}" for name, salary in sorted(lst)), sep="\n")


if __name__ == "__main__":
    main()
