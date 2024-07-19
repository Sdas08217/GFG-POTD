# Count Smaller elements
class Solution:
    def constructLowerArray(self, arr):
        # Step 1: Coordinate Compression
        sorted_arr = sorted(list(set(arr)))
        rank = {val: idx + 1 for idx, val in enumerate(sorted_arr)}

        # Step 2: Binary Indexed Tree (BIT)
        def update(bit, idx, val):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & -idx

        def query(bit, idx):
            total = 0
            while idx > 0:
                total += bit[idx]
                idx -= idx & -idx
            return total

        # Initialize BIT
        n = len(arr)
        bit = [0] * (n + 1)
        ans = [0] * n

        # Step 3: Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            current_rank = rank[arr[i]]
            ans[i] = query(bit, current_rank - 1)
            update(bit, current_rank, 1)
        
        return ans

  # Example usage
sol = Solution()
arr1 = [12, 1, 2, 3, 0, 11, 4]
arr2 = [1, 2, 3, 4, 5]
print(sol.constructLowerArray(arr1))  # Output: [6, 1, 1, 1, 0, 1, 0]
print(sol.constructLowerArray(arr2))  # Output: [0, 0, 0, 0, 0]
