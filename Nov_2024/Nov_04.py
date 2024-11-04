# Find All Triplets with Zero Sum
class Solution:
    def findTriplets(self, arr):
        # Your code here
        from collections import defaultdict
        n = len(arr)
        def collect(i):
            target, m = -arr[i], defaultdict(list)
            for j in range(i+1, n):
                if target - arr[j] in m:
                    for idx in m[target-arr[j]]:
                        yield i, idx, j
                m[arr[j]].append(j)
        for i in range(n):
            yield from collect(i)

# Example array
arr = [0, -1, 2, -3, 1]

# Collect triplets
triplets = list(solution.findTriplets(arr))

# Print results
print("Triplets (by index positions):")
for triplet in triplets:
    print(triplet)

# For a more readable output, printing values instead of indices
print("\nTriplets (by values):")
for triplet in triplets:
    i, j, k = triplet
    print((arr[i], arr[j], arr[k]))
