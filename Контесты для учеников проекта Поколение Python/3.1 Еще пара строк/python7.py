"""Contest."""


def main():
    """My function."""
    num_n = int(input())
    actions, last = [], num_n
    function = (lambda x: x - 2, lambda x: x << 2)
    while last != 1:
        if last & 1:
            last -= 1
        if last == 2:
            break
        if last & 3 == 0:
            actions.append(function[0])
        else:
            last -= 2
        actions.append(function[1])
        last >>= 2
    actions.reverse()
    for func in actions:
        last = func(last)
    print(last)


if __name__ == "__main__":
    main()
