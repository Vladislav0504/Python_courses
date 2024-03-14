"""Exam."""


def main() -> dict[str, list[int]]:
    """My function."""
    dict_0 = {"C1": [10, 20, 30, 7, 6, 23, 90],
              "C2": [20, 30, 40, 1, 2, 3, 90, 12], "C3": [12, 34, 20, 21],
              "C4": [22, 54, 209, 21, 7], "C5": [2, 4, 29, 21, 19],
              "C6": [4, 6, 7, 10, 55], "C7": [4, 8, 12, 23, 42],
              "C8": [3, 14, 15, 26, 48], "C9": [2, 7, 18, 28, 18, 28]}
    limit = 20
    return {k: [x for x in lst if x <= limit] for k, lst in dict_0.items()}


if __name__ == "__main__":
    my_dict = main()
    print(my_dict)
