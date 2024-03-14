"""Int function."""


def main():
    """My function."""
    minutes = int(input())
    hours, residual = divmod(minutes, 60)
    print(f"{minutes} мин - это {hours} час {residual} минут.")


if __name__ == "__main__":
    main()
