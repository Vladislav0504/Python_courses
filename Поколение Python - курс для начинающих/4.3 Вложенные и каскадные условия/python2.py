"""Conditions."""


def main():
    """My function."""
    num_1, num_2, num_3 = (int(input()) for _ in range(3))
    if num_1 == num_2 == num_3:
        print("Равносторонний")
    elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
        print("Равнобедренный")
    else:
        print("Разносторонний")


if __name__ == "__main__":
    main()
