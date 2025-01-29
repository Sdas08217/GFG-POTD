class Solution:
    def nQueen(self, n):
        def backtrack(col, diagonals, anti_diagonals, board):
            row = len(board)
            if row == n:
                result.append(board[:])
                return

            for c in range(n):
                if c in col or (row - c) in diagonals or (row + c) in anti_diagonals:
                    continue

                board.append(c + 1)  # Store 1-based index
                col.add(c)
                diagonals.add(row - c)
                anti_diagonals.add(row + c)

                backtrack(col, diagonals, anti_diagonals, board)

                board.pop()
                col.remove(c)
                diagonals.remove(row - c)
                anti_diagonals.remove(row + c)

        result = []
        backtrack(set(), set(), set(), [])
        return result
