# Row with max 1s
class Solution:
	def rowWithMax1s(self,arr):
	    m = 0
	    r = -1
	    for ind, row in enumerate(arr):
	        t = sum(row)
	        if t > m:
	            m = t
	            r = ind
	        if t == len(row):
	            return r
	    return r

# Example usage
matrix = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]

solution = Solution()
result = solution.rowWithMax1s(matrix)
print(f"The row with the maximum number of 1s is: {result}")
