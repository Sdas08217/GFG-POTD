import bisect

class Solution:
    def printKClosest(self, arr, k, x):
        n = len(arr)
        pos = bisect.bisect_left(arr, x)
        left = pos - 1
        if pos < n and arr[pos] == x:
            right = pos + 1
        else:
            right = pos
        
        res = []
        for _ in range(k):
            if left >= 0 and right < n:
                diff_left = abs(arr[left] - x)
                diff_right = abs(arr[right] - x)
                if diff_left < diff_right:
                    res.append(arr[left])
                    left -= 1
                elif diff_left > diff_right:
                    res.append(arr[right])
                    right += 1
                else:
                    # When diffs are equal, prefer the **larger value**
                    if arr[left] > arr[right]:
                        res.append(arr[left])
                        left -= 1
                    else:
                        res.append(arr[right])
                        right += 1
            elif left >= 0:
                res.append(arr[left])
                left -= 1
            elif right < n:
                res.append(arr[right])
                right += 1
            else:
                break
        return res
