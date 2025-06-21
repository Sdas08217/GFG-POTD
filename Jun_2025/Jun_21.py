from collections import deque

class Solution:
    def catchThieves(self, arr, k):
        police = deque()
        thieves = deque()
        result = 0

        for i in range(len(arr)):
            if arr[i] == 'P':
                police.append(i)
            elif arr[i] == 'T':
                thieves.append(i)

            # Check for matching police-thief pairs
            while police and thieves:
                if abs(police[0] - thieves[0]) <= k:
                    result += 1
                    police.popleft()
                    thieves.popleft()
                elif police[0] < thieves[0]:
                    police.popleft()
                else:
                    thieves.popleft()

        return result
