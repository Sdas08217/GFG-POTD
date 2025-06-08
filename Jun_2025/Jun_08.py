class Solution:
    def isSumString(self, s: str) -> bool:
        n = len(s)
        # Try every possible split point i,j for the first two numbers:
        for i in range(1, n - 1):
            if s[0] == '0' and i > 1:
                break
            
            for j in range(i + 1, n):
                if s[i] == '0' and j - i > 1:
                    break
                
                num1 = int(s[0:i])
                num2 = int(s[i:j])
                
                k = j
                count = 2  # we've already got two numbers
                while k < n:
                    num3 = num1 + num2
                    sum_str = str(num3)
                    L = len(sum_str)
                    
                    if k + L > n or s[k:k+L] != sum_str:
                        break
                    
                    k += L
                    num1, num2 = num2, num3
                    count += 1
                
                if k == n and count >= 3:
                    return True
        
        return False
