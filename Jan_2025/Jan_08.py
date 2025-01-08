class Solution:
    # Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # Sort the array
        arr.sort()
        n = len(arr)
        count = 0

        # Iterate for each k (largest side)
        for k in range(2, n):
            i, j = 0, k - 1
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    # All pairs between i and j are valid
                    count += (j - i)
                    j -= 1
                else:
                    i += 1

        return count
