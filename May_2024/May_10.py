# Combination Sum II

class Solution:
    def CombinationSum2(self, arr, n, k):
        ans = []
        arr.sort()
        def fun(idx, comb, s):
            if idx == n or s > k:
                if s == k:
                    ans.append(comb)
                return

            if s == k:
                ans.append(comb)
                return

            for i in range(idx, n):
                if i > idx and arr[i - 1] == arr[i]:
                    continue
                s += arr[i]
                fun(i + 1, comb + [arr[i]], s)
                s -= arr[i]
        fun(0, [], 0)
        return ans

  # Example usage
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()

    # Test case
    arr = [10, 1, 2, 7, 6, 1, 5]
    k = 8

    # Find all unique combinations
    result = solution.CombinationSum2(arr, len(arr), k)

    # Print the result
    print("Unique combinations that sum up to", k, ":", result)
