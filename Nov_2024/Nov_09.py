# Minimum sum
class Solution:
    def minSum(self, arr):
        # Sort the array to form the smallest numbers
        arr.sort()
        N = len(arr)
        # Two strings for storing our two minimum numbers
        a, b = "", ""
     
        # Create two numbers by alternating digits
        for i in range(0, N, 2):
            a += str(arr[i])
        for i in range(1, N, 2):
            b += str(arr[i])
     
        # Pointers for a and b
        j = len(a) - 1
        k = len(b) - 1
        # Variable to store the carry
        carry = 0
        ans = []
        # Add corresponding digits from a and b
        while j >= 0 and k >= 0:
            sum_digits = (ord(a[j]) - ord('0')) + (ord(b[k]) - ord('0')) + carry
            ans.append(str(sum_digits % 10))  # Append the result digit
            carry = sum_digits // 10  # Update carry
            j -= 1
            k -= 1
        # Add remaining digits from a if any
        while j >= 0:
            sum_digits = (ord(a[j]) - ord('0')) + carry
            ans.append(str(sum_digits % 10))  # Append the result digit
            carry = sum_digits // 10  # Update carry
            j -= 1
        # Add remaining digits from b if any
        while k >= 0:
            sum_digits = (ord(b[k]) - ord('0')) + carry
            ans.append(str(sum_digits % 10))  # Append the result digit
            carry = sum_digits // 10  # Update carry
            k -= 1
        # If there's any carry left, add it to the result
        if carry:
            ans.append(str(carry))
        # Remove leading zeroes and reverse the result
        ans = ''.join(ans[::-1]).lstrip('0')
        
        # If the result is empty (i.e., all digits were zero), return '0'
        return ans if ans else '0'


# Instantiate the Solution class
solution = Solution()

# Example array
arr = [6, 8, 4, 5, 2, 3]

# Call the minSum method and print the result
result = solution.minSum(arr)
print("Minimum possible sum:", result)
