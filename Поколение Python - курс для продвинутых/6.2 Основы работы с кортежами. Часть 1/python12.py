"""Tuples."""


def main():
    """My function."""
    tuples = [(), (), ("",), ("a", "b"), (), ("a", "b", "c"), (1,), (), (),
              ("d",), ("", ""), ()]
    non_empty_tuples = [elem for elem in tuples if elem]
    print(non_empty_tuples)


if __name__ == "__main__":
    main()
