# K-Palindrome
class Solution:
    def kPalindrome(self, st, n, k):
        prev=[0]*len(st)
        for i in range(len(st)-1,-1,-1):
            curr=[0]*len(st)
            curr[i]=1
            for j in range(i+1,len(st)):
                curr[j]=max(prev[j],curr[j-1])
                if st[i]==st[j]:
                    curr[j]=max(curr[j],2+prev[j-1])
            prev=[l for l in curr]
        return 1 if len(st)-curr[len(st)-1]<=k else 0
# Example usage:
sol = Solution()
st = "abcdecba"
n = len(st)
k = 2
print(sol.kPalindrome(st, n, k))  # Output will be 1 if the string can be transformed into a k-palindrome, else 0
