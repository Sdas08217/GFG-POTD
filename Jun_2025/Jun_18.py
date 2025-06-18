class Solution:
    def palinParts(self, s):
        result = []

        # Helper function to check if a string is palindrome
        def is_palindrome(sub):
            return sub == sub[::-1]

        # Backtracking function to find palindrome partitions
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()  # backtrack

        backtrack(0, [])
        return result
