# Circle of strings
from collections import defaultdict

class Solution:
    def dfs(self, node, visited, graph):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, graph)

    def is_strongly_connected(self, graph, reverse_graph, starting_vertex, num_chars):
        visited = [False] * num_chars
        self.dfs(starting_vertex, visited, graph)

        # Check if all vertices with edges are visited
        for i in range(num_chars):
            if len(graph[i]) > 0 and not visited[i]:
                return False

        # Reset visited and run DFS on the reverse graph
        visited = [False] * num_chars
        self.dfs(starting_vertex, visited, reverse_graph)

        # Check if all vertices with edges are visited in the reversed graph
        for i in range(num_chars):
            if len(reverse_graph[i]) > 0 and not visited[i]:
                return False

        return True

    def isCircle(self, arr):
        num_chars = 26
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        in_degree = [0] * num_chars
        out_degree = [0] * num_chars

        # Build the graph
        for string in arr:
            start = ord(string[0]) - ord('a')
            end = ord(string[-1]) - ord('a')
            graph[start].append(end)
            reverse_graph[end].append(start)
            out_degree[start] += 1
            in_degree[end] += 1

        # Check if in-degree and out-degree of all vertices match
        for i in range(num_chars):
            if in_degree[i] != out_degree[i]:
                return 0

        # Find a starting vertex with an edge
        starting_vertex = -1
        for i in range(num_chars):
            if out_degree[i] > 0:
                starting_vertex = i
                break

        # Check if the graph is strongly connected
        if starting_vertex == -1:
            return 0

        if not self.is_strongly_connected(graph, reverse_graph, starting_vertex, num_chars):
            return 0

        return 1

  #Eaxmple Usage
  # Example usage of the Solution class
sol = Solution()

# Test case 1: Strings cannot form a circle
arr1 = ["abc", "bcd", "cdf"]
result1 = sol.isCircle(arr1)
print(f"Can the strings {arr1} form a circle? {'Yes' if result1 == 1 else 'No'}")  # Output: No

# Test case 2: Strings can form a circle
arr2 = ["ab", "bc", "cd", "da"]
result2 = sol.isCircle(arr2)
print(f"Can the strings {arr2} form a circle? {'Yes' if result2 == 1 else 'No'}")  # Output: Yes

# Test case 3: Another case where strings can form a circle
arr3 = ["for", "geek", "rig", "kaf"]
result3 = sol.isCircle(arr3)
print(f"Can the strings {arr3} form a circle? {'Yes' if result3 == 1 else 'No'}")  # Output: Yes

# Test case 4: Single string
arr4 = ["aaa"]
result4 = sol.isCircle(arr4)
print(f"Can the string {arr4} form a circle? {'Yes' if result4 == 1 else 'No'}")  # Output: Yes

# Test case 5: Strings cannot form a circle
arr5 = ["abc", "xyz"]
result5 = sol.isCircle(arr5)
print(f"Can the strings {arr5} form a circle? {'Yes' if result5 == 1 else 'No'}")  # Output: No
