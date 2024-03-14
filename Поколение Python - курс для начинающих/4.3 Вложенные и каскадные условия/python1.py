"""Conditions."""


def main():
    """My function."""
    velocity_n, velocity_k = int(input()), int(input())
    if velocity_n > velocity_k:
        print("NO")
    elif velocity_k > velocity_n:
        print("YES")
    else:
        print("Don't know")


if __name__ == "__main__":
    main()
