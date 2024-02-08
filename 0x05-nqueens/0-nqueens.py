#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an NxN chessboard. Write a program that solves the N queens problem.
"""


import sys


def generate_solutions(row, column):
    """
    Generate solutions for the N Queens problem using backtracking.

    Args:
        row (int): The current row to place the queen.
        column (int): The size of the chessboard (number of columns).

    Returns:
        list: List of solutions, where each solution is represented as
        a list of column indices.
    """
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    """
    Place a queen on the chessboard at the specified row
    and generate safe positions.

    Args:
        queen (int): The current row to place the queen.
        column (int): The size of the chessboard (number of columns).
        prev_solution (list): List of previous solutions.

    Returns:
        list: List of safe positions for the queen in the current row.
    """
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """
    Check if it's safe to place a queen at the specified position.

    Args:
        q (int): The row index of the queen.
        x (int): The column index to check.
        array (list): The current state of the chessboard.

    Returns:
        bool: True if it's safe to place a queen at the specified position,
        False otherwise.
    """
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column for column in range(q))


def init():
    """
    Initialize the N value and perform error checks
    on the command-line argument.

    Returns:
        int: The size of the chessboard (number of rows/columns).
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def n_queens():
    """
    Main function to solve the N Queens problem and print solutions.
    """
    n = init()
    # generate all solutions
    solutions = generate_solutions(n, n)
    # print solutions
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
