"""Contest."""


def choose_plural(num: int, lst: [str, str, str]) -> str:
    """Choose plural."""
    num = str(num)
    if num[-1] == "1" and num[-2:] != "11":
        return " ".join((num, lst[0]))
    if num[-1] in "234" and num[-2:] not in "121314":
        return " ".join((num, lst[1]))
    return " ".join((num, lst[2]))


def main():
    """My function."""
    assert choose_plural(21, ["пример", "примера", "примеров"]) == "21 пример"
    assert choose_plural(92, ["гвоздь", "гвоздя", "гвоздей"]) == "92 гвоздя"
    assert choose_plural(8, ["яблоко", "яблока", "яблок"]) == "8 яблок"


if __name__ == "__main__":
    main()
