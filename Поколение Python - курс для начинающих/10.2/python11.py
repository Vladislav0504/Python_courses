"""Exam."""


def main():
    """My function."""
    string = input()
    ind_1, ind_2 = string.find("h"), string.rfind("h")
    print(string[:ind_1 + 1] + string[ind_1 + 1:ind_2][::-1] + string[ind_2:])


if __name__ == "__main__":
    main()
