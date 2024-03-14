"""Loops."""


def main():
    """My function."""
    for num_n in range(1, 11):
        for num_k in range(1, 11):
            for num_m in range(1, 10):
                if 28 * num_n + 30 * num_k + 31 * num_m == 365:
                    print(f"n = {num_n}, k = {num_k}, m = {num_m}")


if __name__ == "__main__":
    main()
