class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        rowSum = [0] * n
        colSum = [0] * n

        # Step 1: Calculate row and column sums
        for i in range(n):
            for j in range(n):
                rowSum[i] += mat[i][j]
                colSum[j] += mat[i][j]

        # Step 2: Find the target sum (maximum of all row and column sums)
        target = max(max(rowSum), max(colSum))

        # Step 3: Count total operations required to make each row sum equal to target
        # Since only increment operations are allowed, we bring each row up to target
        total_operations = 0
        for i in range(n):
            total_operations += (target - rowSum[i])

        return total_operations
