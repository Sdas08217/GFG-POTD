# Nearest multiple of 10
import sys
class Solution:
    def roundToNearest (self, num_str) :
        sys.set_int_max_str_digits(100000)
        ol = len(num_str)  
    
        num = int(num_str)
        
        lastdigit = num % 10
       
        if lastdigit > 5:  
            rounded_num = num + (10 - lastdigit)  
        else:
            rounded_num = num - lastdigit  
        
        ans = str(rounded_num)  
        nl = len(ans)  
        extraZ = ol - nl
        newans = '0' * extraZ 
        newans += ans
        return newans
#Example Usage

  # Create an instance of the Solution class
sol = Solution()

# Call the roundToNearest method with a string number
result = sol.roundToNearest("12345678901234567890")

# Print the result
print(result)
