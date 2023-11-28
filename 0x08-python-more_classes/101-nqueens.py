#!/usr/bin/python3
""" The N queens puzzle challange """

import sys


def initialize_board(x):
    """ Create an empty `n`x`n` chessboard. """
    board = []
    [board.append([]) for i in range(x)]
    [row.append(' ') for i in range(x) for row in board]
    return (board)


def deepcopy_board(b):
    """ Return a deep copy of the chessboard. """
    if isinstance(b, list):
        return list(map(deepcopy_board, b))
    return (b)


def solution(b):
    """ Return the solved chessboard as a list of lists. """
    solution = []
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i][j] == "Q":
                solution.append([i, j])
                break
    return (solution)


def mark_attacked_spots(b, r, c):
    """
    Marking Non-Attacking Queen Positions on Chessboard

    Args:
    - b (list): The current chessboard configuration.
    - r (int): The row where the last queen was placed.
    - c (int): The column where the last queen was placed.
    """

    # X out all forward spots
    for c in range(c + 1, len(b)):
        b[r][c] = "x"
    # X out all backwards spots
    for c in range(c - 1, -1, -1):
        b[r][c] = "x"
    # X out all spots below
    for r in range(r + 1, len(b)):
        b[r][c] = "x"
    # X out all spots above
    for r in range(r - 1, -1, -1):
        b[r][c] = "x"
    # X out all spots diagonally down to the right
    c = c + 1
    for r in range(r + 1, len(b)):
        if c >= len(b):
            break
        b[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = c - 1
    for r in range(r - 1, -1, -1):
        if c < 0:
            break
        b[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = c + 1
    for r in range(r - 1, -1, -1):
        if c >= len(b):
            break
        b[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = c - 1
    for r in range(r + 1, len(b)):
        if c < 0:
            break
        b[r][c] = "x"
        c -= 1


def solve(b, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        b (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(b):
        solutions.append(solution(b))
        return (solutions)

    for c in range(len(b)):
        if b[row][c] == " ":
            tmp_b = deepcopy_board(b)
            tmp_b[row][c] = "Q"
            mark_attacked_spots(tmp_b, row, c)
            solutions = solve(tmp_b, row + 1,
                              queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = initialize_board(int(sys.argv[1]))
    solutions = solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
