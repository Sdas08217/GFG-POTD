# Swap two nibbles in a byte
class Solution:
    def swapNibbles(self, n):
        # Extract the high nibble (shift right by 4)
        high_nibble = (n & 0xF0) >> 4
        # Extract the low nibble (AND with 0x0F)
        low_nibble = (n & 0x0F)
        # Swap the nibbles by shifting low nibble left by 4 and combining with high nibble
        swapped = (low_nibble << 4) | high_nibble
        return swapped
      # Example usage
solution = Solution()
print(solution.swapNibbles(100))  # Output: 70
print(solution.swapNibbles(129))  # Output: 24
