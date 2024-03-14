"""Strings."""


def main():
    """My function."""
    string = input()
    ind_1, ind_2 = string.find("f"), string.rfind("f")
    lst = [ind_1]
    if ind_1 != ind_2:
        lst.append(ind_2)
    print(*("NO",) if ind_1 == -1 else lst)


if __name__ == "__main__":
    main()
