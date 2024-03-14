"""Complex numbers."""


def main():
    """My function."""
    num_n, z_1, z_2 = int(input()), complex(input()), complex(input())
    z_11, z_21 = z_1.conjugate(), z_2.conjugate()
    result = z_1**num_n + z_2**num_n + z_11**num_n + z_21**(num_n + 1)
    print(result)


if __name__ == "__main__":
    main()
