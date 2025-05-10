class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        # 1) Build prefix sums P[0..n]:
        #    +1 for a[i] > k, -1 otherwise
        P = [0] * (n+1)
        for i, val in enumerate(arr):
            P[i+1] = P[i] + (1 if val > k else -1)
        # 2) Build a stack of candidate start‐indices
        #    (strictly decreasing P[i])
        st = []
        for i in range(n+1):
            if not st or P[i] < P[st[-1]]:
                st.append(i)
        # 3) Scan j = n..0, popping any start i with P[i] < P[j]
        #    and updating the max length j - i
        res = 0
        for j in range(n, -1, -1):
            while st and P[st[-1]] < P[j]:
                i = st.pop()
                res = max(res, j - i)
        return res
