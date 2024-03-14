"""Contest."""


def likes(lst: list[str]) -> str:
    """Likes."""
    if not lst:
        return "Никто не оценил данную запись"
    if len(lst) == 1:
        return f"{lst[0]} оценил данную запись"
    if len(lst) == 2:
        return f"{lst[0]} и {lst[1]} оценили данную запись"
    if len(lst) == 3:
        return f"{lst[0]}, {lst[1]} и {lst[2]} оценили данную запись"
    num = len(lst) - 2
    return f"{lst[0]}, {lst[1]} и {num} других оценили данную запись"


def main():
    """My function."""
    assert likes([]) == "Никто не оценил данную запись"
    assert likes(["Тимур"]) == "Тимур оценил данную запись"
    assert likes(["Тимур", "Артур"]) == "Тимур и Артур оценили данную запись"
    assert likes(["Тимур", "Артур",
                  "Руслан"]) == "Тимур, Артур и Руслан оценили данную запись"
    assert likes(["Тимур", "Артур", "Руслан",
                  "Анри"]) == "Тимур, Артур и 2 других оценили данную запись"


if __name__ == "__main__":
    main()
