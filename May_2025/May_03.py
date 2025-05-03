import bisect

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    _sieve = None
    _primes = None

    def __init__(self):
        if Solution._sieve is None:
            max_limit = 100000
            sieve = [False, False] + [True] * (max_limit - 1)
            for i in range(2, int(max_limit ** 0.5) + 1):
                if sieve[i]:
                    for j in range(i * i, max_limit + 1, i):
                        sieve[j] = False
            Solution._sieve = sieve
            Solution._primes = [i for i, is_p in enumerate(sieve) if is_p]

    def primeList(self, head):
        current = head
        sieve = Solution._sieve
        primes = Solution._primes

        while current:
            val = current.val
            if val < len(sieve) and sieve[val]:
                current = current.next
                continue  # Already prime

            # Find nearest prime using binary search
            idx = bisect.bisect_left(primes, val)
            left = primes[idx - 1] if idx > 0 else float('-inf')
            right = primes[idx] if idx < len(primes) else float('inf')

            # Compare distances
            if abs(left - val) <= abs(right - val):
                current.val = left
            else:
                current.val = right

            current = current.next

        return head
