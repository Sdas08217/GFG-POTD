# Edit Distance
class Solution:
	def editDistance(self, str1, str3):
		N , M = len(str1), len(str3)
		dp = [[0] * (M + 1) for _ in range(N + 1)]
		for i in range(N + 1):
		    for j in range(M + 1):
		        if i == 0 or j == 0:
		            dp[i][j] = i + j
		        else:
		            if str1[i - 1] == str3[j - 1]:
		                dp[i][j] = dp[i - 1][j - 1]
		            else:
		                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1],dp[i - 1][j - 1])
		return dp[N][M]

# Example usage
solution = Solution()
str1 = "kitten"
str3 = "sitting"
result = solution.editDistance(str1, str3)
print(f"The edit distance between '{str1}' and '{str3}' is {result}.")
