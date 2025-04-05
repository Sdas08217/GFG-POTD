class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        # 8 possible directions (horizontal, vertical, diagonal)
        dx = [-1, -1, -1,  0, 0, 1, 1, 1]
        dy = [-1,  0,  1, -1, 1, -1, 0, 1]

        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < m and grid[x][y] == 'L' and not visited[x][y]

        def dfs(x, y):
            visited[x][y] = True
            for dir in range(8):
                new_x, new_y = x + dx[dir], y + dy[dir]
                if is_valid(new_x, new_y):
                    dfs(new_x, new_y)

        island_count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L' and not visited[i][j]:
                    dfs(i, j)
                    island_count += 1

        return island_count
