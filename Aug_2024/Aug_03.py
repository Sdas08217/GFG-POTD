# The Celebrity Problem
Difficulty: MediumAccuracy: 38.3
class Solution:
    def celebrity(self, mat):
        for i in range(len(mat)):
            a=1
            for j in range(len(mat)):
                if mat[i][j]==1:
                    a=0
                    break
            if a==1:
                for j in range(len(mat)):
                    if i!=j and mat[j][i]==0:
                        a=0
                        break
            if a==1:
                return i
        return -1

  # Example usage:
mat = [
    [0, 1, 1],
    [0, 0, 0],
    [1, 1, 0]
]

solution = Solution()
celebrity_index = solution.celebrity(mat)

if celebrity_index != -1:
    print(f"Celebrity found at index: {celebrity_index}")
else:
    print("No celebrity found")
