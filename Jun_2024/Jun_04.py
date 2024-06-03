# Binary representation of next number
class Solution:
    def binaryNextNumber(self, s):
        # Convert the binary string to a list of characters for easier manipulation
        binary_list = list(s)
        n = len(binary_list)
        
        # Traverse the binary string from right to left
        for i in range(n-1, -1, -1):
            if binary_list[i] == '0':
                binary_list[i] = '1'
                break
            else:
                binary_list[i] = '0'
        else:
            # If we exit the loop without breaking, it means all bits were '1'
            # Hence we need an extra bit at the start
            binary_list.insert(0, '1')
        
        # Join the list back into a string and strip leading zeros
        result = ''.join(binary_list)
        return result.lstrip('0') or '0'
      # Example usage:
solution = Solution()
print(solution.binaryNextNumber("10"))       # Output: "11"
print(solution.binaryNextNumber("111"))      # Output: "1000"
print(solution.binaryNextNumber("0011111100"))  # Output: "11111101"
