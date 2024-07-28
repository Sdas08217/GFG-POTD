# Remove Duplicates
class Solution:
    def removeDups(self, str):

        unique_alpha = [0] * 26
        result = ''

        for i in range(len(str)): 
            if unique_alpha[ord(str[i]) - 97] == 0: 
                result += str[i]
                unique_alpha[ord(str[i]) - 97] += 1

        return result

  
# Example usage
sol = Solution()
input_str = "hello"
output_str = sol.removeDups(input_str)
print(f"Input: {input_str}")
print(f"Output: {output_str}")
