# Nuts and Bolts Problem
class Solution:
 
   def matchPairs(self, n, nuts, bolts):
        order = [ '!','#','$','%','&','*','?','@','^']
        n = []
        for i in order:
            if i in nuts and i in bolts:
                n.append(i)
        nuts[:] = n
        bolts[:] = n

# Example usage:
nuts = ['@', '%', '&']
bolts = ['&', '%', '@']
n = len(nuts)

solution = Solution()
solution.matchPairs(n, nuts, bolts)

print("Nuts: ", nuts)
print("Bolts: ", bolts)
