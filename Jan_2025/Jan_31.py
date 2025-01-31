class Solution:
    
    def solveSudoku(self, board):
        """Solves Sudoku using Backtracking with Constraint Propagation"""
        
        # Sets to track constraints
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Initialize sets and find empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def backtrack(index):
            """Backtracking with Most Constrained Variable First"""
            if index == len(empty_cells):  # All cells filled
                return True

            r, c = empty_cells[index]
            box_id = (r // 3) * 3 + (c // 3)

            for num in range(1, 10):
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_id]:
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_id].add(num)

                    if backtrack(index + 1):
                        return True

                    # Undo the move (backtrack)
                    board[r][c] = 0
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_id].remove(num)

            return False  # No valid number found, trigger backtracking

        backtrack(0)

    def printSudoku(self, board):
        """Prints the Sudoku board"""
        for row in board:
            print(" ".join(map(str, row)))
