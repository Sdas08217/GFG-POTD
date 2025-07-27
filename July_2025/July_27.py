class Solution:
    def setMatrixZeroes(self, mat):
        n = len(mat)
        m = len(mat[0])
        rows = set()
        cols = set()

        # First pass: record rows and columns that contain a zero
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Second pass: update the matrix
        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    mat[i][j] = 0

        return mat
