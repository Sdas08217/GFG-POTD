from collections import defaultdict, deque

class Solution:
    @staticmethod
    def findOrder(words):
        # Step 1: Build the graph and in-degree
        graph = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Invalid prefix case, e.g., "abc" and "ab"
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        # Step 2: Topological sort (Kahn's algorithm)
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        result = []

        while queue:
            ch = queue.popleft()
            result.append(ch)
            for neighbor in graph[ch]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 3: Check for cycle
        if len(result) != len(in_degree):
            return ""

        return "".join(result)
