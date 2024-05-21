from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []  # Initialize an empty list to store tuples of (row/col/box, value)

        # Iterate over each cell in the Sudoku board
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != ".":  # Ignore empty cells
                    # Add tuples representing the value's presence in row, column, and 3x3 box
                    res += [(i, x), (x, j), (i // 3, j // 3, x)]

        # Check if the length of the list of tuples is equal to the length of the set of tuples
        # If they are equal, it means there are no duplicates, and the Sudoku board is valid
        return len(res) == len(set(res))
