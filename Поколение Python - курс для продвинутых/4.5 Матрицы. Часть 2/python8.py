"""Matrices."""


def main():
    """My function."""
    coord, size = input(), 8
    board = tuple(["."] * size for _ in range(size))
    col, row = ord(coord[0]) - ord("a"), size - int(coord[1])
    board[row][col] = "N"
    for i, line in enumerate(board):
        for j in range(size):
            if abs(row - i) * abs(col - j) == 2:
                line[j] = "*"
        print(*line)


if __name__ == "__main__":
    main()
