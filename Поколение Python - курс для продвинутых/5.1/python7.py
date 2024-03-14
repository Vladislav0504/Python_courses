"""Exam."""


def main():
    """My function."""
    coord, size = input(), 8
    board = tuple(["."] * size for _ in range(size))
    col, row = ord(coord[0]) - ord("a"), size - int(coord[1])
    for i in range(size):
        board[i][col] = "*"
        board[row][i] = "*"
        if 0 <= row + col - i < size:
            board[i][row + col - i] = "*"
        if 0 <= i - row + col < size:
            board[i][i - row + col] = "*"
    board[row][col] = "Q"
    for elem in board:
        print(*elem)


if __name__ == "__main__":
    main()
