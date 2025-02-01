class Solution:
    def isWordExist(self, mat, word):
        n, m = len(mat), len(mat[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        
        def dfs(x, y, index):
            """Backtracking DFS function to search for the word."""
            if index == len(word):  # If we have matched all characters
                return True
            
            if not (0 <= x < n and 0 <= y < m) or mat[x][y] != word[index]:
                return False  # Out of bounds or character mismatch
            
            # Temporarily mark the cell as visited
            temp, mat[x][y] = mat[x][y], '#'
            
            for dx, dy in directions:
                if dfs(x + dx, y + dy, index + 1):
                    return True
            
            # Backtrack and restore the cell
            mat[x][y] = temp
            return False
        
        # Find the starting points and call DFS
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0]:  # Start DFS if first letter matches
                    if dfs(i, j, 0):
                        return True
        
        return False
