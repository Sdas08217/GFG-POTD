class Solution:
    def getSingle(self, arr):
        result = 0
        for i in range(32):  # Assuming 32-bit integers
            bit_sum = 0
            for num in arr:
                if (num >> i) & 1:
                    bit_sum += 1
            if bit_sum % 3:
                result |= (1 << i)
        
        # Adjust for negative numbers (two's complement)
        if result >= 2**31:
            result -= 2**32
        return result
