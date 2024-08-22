# Alien Dictionary
class Solution:
    def findOrder(self, words, num_words, alphabet_size):
        # Create an adjacency list for characters in the words
        adj_list = {char: set() for word in words for char in word}

        # Build the graph by comparing adjacent words in the dictionary
        for i in range(num_words - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))

            # Edge case: if word1 is a prefix of word2 but longer, the order is invalid
            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return ""

            # Find the first differing character between word1 and word2 and create a directed edge
            for j in range(min_length):
                if word1[j] != word2[j]:
                    adj_list[word1[j]].add(word2[j])
                    break

        visited = {}  # Dictionary to track visited nodes in DFS
        order = []    # List to store the topological order of characters

        # Depth First Search (DFS) to detect cycles and build topological order
        def dfs(char):
            if char in visited:  # If already visited, return its state (True for cycle, False for safe)
                return visited[char]

            visited[char] = True  # Mark the node as visited (currently being explored)
            for neighbor in adj_list[char]:
                if dfs(neighbor):  # If a cycle is detected, return True
                    return True

            visited[char] = False  # Mark the node as safe after exploration
            order.append(char)  # Add the character to the order list

        # Perform DFS for each character in the graph
        for char in adj_list:
            if dfs(char):  # If a cycle is found, the order is invalid
                return ""

        # Return the reverse of the order list as a string (to get the correct topological order)
        return "".join(order[::-1])


# Example usage of the Solution class
words = ["wrt", "wrf", "er", "ett", "rftt"]
num_words = len(words)
alphabet_size = 5  # Assuming we know the alphabet size (this could vary)

# Create an instance of the Solution class
solution = Solution()

# Find the order of characters in the alien dictionary
order = solution.findOrder(words, num_words, alphabet_size)

# Output the result
print(order)  # Output should be a valid order like "wertf"
