"""Problems."""


def act(n_1: float, n_2: float, action: str) -> float:
    """My action."""
    if action == "-":
        n_2 = -n_2
    elif action == "/":
        n_2 = 1 / n_2
        action = "*"
    if action == "*":
        return n_1 * n_2
    if action == "mod":
        return n_1 % n_2
    if action == "pow":
        return n_1**n_2
    if action == "div":
        return n_1 // n_2
    return n_1 + n_2


def main():
    """My function."""
    n_1, n_2, string = float(input()), float(input()), input()
    if string in ("/", "mod", "div") and n_2 == 0:
        print("Деление на 0!")
    else:
        print(act(n_1, n_2, string))


if __name__ == "__main__":
    main()
