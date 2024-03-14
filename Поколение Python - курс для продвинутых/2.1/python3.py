"""Repetition."""


def main():
    """My function."""
    string, cost_per_char, kopecks_in_rubles = input(), 60, 100
    cost = cost_per_char * len(string)
    rubles, kopecks = divmod(cost, kopecks_in_rubles)
    print(f"{rubles} р. {kopecks} коп.")


if __name__ == "__main__":
    main()
