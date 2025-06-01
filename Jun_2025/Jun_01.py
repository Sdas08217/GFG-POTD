class Solution:
    def countPairs(self, mat1, mat2, x):
        n = len(mat1)  # Assuming mat1 and mat2 are both n x n
        set1 = set()
        count = 0

        # Insert all elements from mat1 into a set for quick lookup
        for i in range(n):
            for j in range(n):
                set1.add(mat1[i][j])

        # Check if x - mat2[i][j] exists in set1
        for i in range(n):
            for j in range(n):
                if (x - mat2[i][j]) in set1:
                    count += 1

        return count
