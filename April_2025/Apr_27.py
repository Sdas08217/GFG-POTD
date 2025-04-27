class Solution:
    def multiplyStrings(self, s1, s2):
        # Helper to remove leading zeros
        def strip_leading_zeros(s):
            i = 0
            while i < len(s) and s[i] == '0':
                i += 1
            return s[i:] if i != len(s) else '0'
        
        # Check if the result will be negative
        neg = False
        if s1 and s1[0] == '-':
            neg = not neg
            s1 = s1[1:]
        if s2 and s2[0] == '-':
            neg = not neg
            s2 = s2[1:]
        
        s1 = strip_leading_zeros(s1)
        s2 = strip_leading_zeros(s2)
        
        # If either is "0"
        if s1 == "0" or s2 == "0":
            return "0"
        
        # Create result array
        res = [0] * (len(s1) + len(s2))
        
        # Manual multiplication
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                n1 = ord(s1[i]) - ord('0')
                n2 = ord(s2[j]) - ord('0')
                mul = n1 * n2
                sum_ = mul + res[i + j + 1]
                res[i + j + 1] = sum_ % 10
                res[i + j] += sum_ // 10
        
        # Skip leading zeros
        result = []
        leading_zero = True
        for num in res:
            if leading_zero and num == 0:
                continue
            leading_zero = False
            result.append(chr(num + ord('0')))
        
        final_result = ''.join(result)
        
        if neg:
            final_result = '-' + final_result
            
        return final_result
