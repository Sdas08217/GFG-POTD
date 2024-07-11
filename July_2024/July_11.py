# Maximum Connected group
from typing import List

class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        
        def dfs(x, y, visited, component_id):
            stack = [(x, y)]
            size = 0
            while stack:
                cx, cy = stack.pop()
                if visited[cx][cy]:
                    continue
                visited[cx][cy] = True
                size += 1
                component_map[cx][cy] = component_id
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                        stack.append((nx, ny))
            return size
        
        visited = [[False] * n for _ in range(n)]
        component_map = [[-1] * n for _ in range(n)]
        component_sizes = []
        component_id = 0
        
        # Identify all components of 1's and their sizes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    size = dfs(i, j, visited, component_id)
                    component_sizes.append(size)
                    component_id += 1
        
        # If there are no 1's, the best we can do is changing one 0 to 1
        if not component_sizes:
            return 1
        
        # Find the maximum size of connected 1's after changing one 0 to 1
        max_size = max(component_sizes)
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    unique_components = set()
                    current_size = 1
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                            comp_id = component_map[nx][ny]
                            if comp_id not in unique_components:
                                unique_components.add(comp_id)
                                current_size += component_sizes[comp_id]
                    max_size = max(max_size, current_size)
        
        return max_size

  # Example 1
grid1 = [
    [1, 1],
    [0, 1]
]

solution = Solution()
result1 = solution.MaxConnection(grid1)
print(result1)  # Output: 4

# Example 2
grid2 = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1]
]

result2 = solution.MaxConnection(grid2)
print(result2)  # Output: 7
