"""Complex numbers."""


def main():
    """My function."""
    num_1, num_2 = complex(input()), complex(input())
    my_dict = {"+": num_1 + num_2, "-": num_1 - num_2, "*": num_1 * num_2}
    print(*(f"{num_1} {sign} {num_2} = {result}"
            for sign, result in my_dict.items()), sep="\n")


if __name__ == "__main__":
    main()
