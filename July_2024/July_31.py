# Longest Common Prefix of Strings
class Solution:
    def longestCommonPrefix(self, arr):
        if not arr:
            return "-1"
        
        # Start with the first string as the prefix
        prefix = arr[0]
        
        for string in arr[1:]:
            # Compare characters one by one
            i = 0
            while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
                i += 1
            # Update the prefix to the common prefix found so far
            prefix = prefix[:i]
            # If there's no common prefix, return "-1"
            if not prefix:
                return "-1"
        
        return prefix

# Example usage
solution = Solution()
print(solution.longestCommonPrefix(["geeksforgeeks", "geeks", "geek", "geezer"]))  # Output: "gee"
print(solution.longestCommonPrefix(["hello", "world"]))  # Output: "-1"
