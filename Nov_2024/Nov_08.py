# Minimum repeat to make substring
import math
class Solution:
    def minRepeats(self, s1, s2):
        st1 = set(s1)
        st2 = set(s2)
        
        for k in st2:
            if k not in st1:
                return -1
                
        count = 1
        c = len(s2)
        new_s1 = s1
        
        while len(new_s1) <= 2*c:
            if new_s1.find(s2) != -1:
                return count
            count += 1
            new_s1 += s1
            
        if new_s1.find(s2) != -1:
                return count
            
        return -1

  # Example usage
s1 = "abcd"
s2 = "cdabcdab"

solution = Solution()
result = solution.minRepeats(s1, s2)
print(result)  # Output: 3, since repeating "abcd" 3 times results in "abcdabcdabcd" which contains "cdabcdab"
