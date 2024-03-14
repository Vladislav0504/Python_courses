"""Dictionaries."""


def main() -> dict[str, int]:
    """My function."""
    dict_1 = {"a": 100, "z": 333, "b": 200, "c": 300, "d": 45, "e": 98,
              "t": 76, "q": 34, "f": 90, "m": 230}
    dict_2 = {"a": 300, "b": 200, "d": 400, "t": 777, "c": 12, "p": 123,
              "w": 111, "z": 666}
    res = dict_1.copy()
    for key, value in dict_2.items():
        res[key] = res.get(key, 0) + value
    return res


if __name__ == "__main__":
    result = main()
    print(result)
