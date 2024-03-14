"""Loops."""


def main():
    """My function."""
    max_num = 151
    d_5 = [i**5 for i in range(max_num)]
    for _a in range(1, max_num):
        for _b in range(_a, max_num):
            for _c in range(_b, max_num):
                for _d in range(_c, max_num):
                    result = d_5[_a] + d_5[_b] + d_5[_c] + d_5[_d]
                    if result == int(result**0.2)**5:
                        _e = int(result**0.2)
                        print(f"Решение: {_a}, {_b}, {_c}, {_d}, {_e}.")
                        print(_a + _b + _c + _d + _e)


if __name__ == "__main__":
    main()
