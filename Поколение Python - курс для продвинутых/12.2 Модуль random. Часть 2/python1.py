"""Random."""
from random import randrange


def generate_ip() -> str:
    """Generate ip address."""
    limit = 256
    return ".".join(str(randrange(limit)) for _ in range(4))


def main():
    """My function."""
    print(generate_ip())


if __name__ == "__main__":
    main()
