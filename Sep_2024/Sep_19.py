# Reverse Words
class Solution:
    
    # Function to reverse words in a given string.
    def reverseWords(self, s: str) -> str:
        # Split the string by dots to get individual words
        words = s.split('.')
        # Reverse the list of words
        words.reverse()
        # Join the reversed words with dots and return the result
        return '.'.join(words)

  #Example Usage
# Create an instance of the Solution class
solution = Solution()

# Input string
s = "hello.world.this.is.example"

# Call the reverseWords function
result = solution.reverseWords(s)

# Output the result
print(result)
