# N-Queen Problem
class Solution:
    def nQueen(self, n):
        def backtrack(row, cols, diagonals1, diagonals2, current_solution):
            if row == n:
                solutions.append(current_solution[:])
                return
            
            for col in range(n):
                diag1 = row - col
                diag2 = row + col
                
                if col in cols or diag1 in diagonals1 or diag2 in diagonals2:
                    continue
                
                cols.add(col)
                diagonals1.add(diag1)
                diagonals2.add(diag2)
                current_solution.append(col + 1)
                
                backtrack(row + 1, cols, diagonals1, diagonals2, current_solution)
                
                current_solution.pop()
                cols.remove(col)
                diagonals1.remove(diag1)
                diagonals2.remove(diag2)
        
        solutions = []
        backtrack(0, set(), set(), set(), [])
        return solutions

  # Example usage:
sol = Solution()
print(sol.nQueen(1))  # Output: [[1]]
print(sol.nQueen(4))  # Output: [[2, 4, 1, 3], [3, 1, 4, 2]]
