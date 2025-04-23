class Solution:
    def singleNum(self, arr):
        xor_all = 0
        for num in arr:
            xor_all ^= num

        # Get the rightmost set bit in xor_all
        set_bit = xor_all & -xor_all

        num1 = 0
        num2 = 0

        # Divide elements into two groups based on the set_bit
        for num in arr:
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num

        return sorted([num1, num2])
