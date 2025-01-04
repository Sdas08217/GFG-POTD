class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        count = 0
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                sum_triplet = arr[i] + arr[j] + arr[k]
                if sum_triplet == target:
                    # If sum_triplet is equal to target, count all pairs (j, k) that sum up to the target
                    left = j
                    right = k
                    if arr[j] == arr[k]:
                        count += (k - j + 1) * (k - j) // 2
                        break
                    left_count = 1
                    right_count = 1
                    while j + 1 < k and arr[j] == arr[j + 1]:
                        left_count += 1
                        j += 1
                    while k - 1 > j and arr[k] == arr[k - 1]:
                        right_count += 1
                        k -= 1
                    count += left_count * right_count
                    j += 1
                    k -= 1
                elif sum_triplet < target:
                    j += 1
                else:
                    k -= 1
        return count
