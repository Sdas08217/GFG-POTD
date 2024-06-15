# Prime Pair with Target Sum

from typing import List
class Solution:
    def getPrimes(self, n: int) -> List[int]:
        if n < 3:
            return [-1, -1]

        # Sieve of Eratosthenes to find all primes up to n
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        
        for start in range(2, int(n**0.5) + 1):
            if sieve[start]:
                for multiple in range(start*start, n + 1, start):
                    sieve[multiple] = False
        
        # List of primes
        primes = [num for num, is_prime in enumerate(sieve) if is_prime]

        # Check for pairs
        for prime in primes:
            if prime > n - prime:
                break
            if sieve[n - prime]:
                return [prime, n - prime]

        return [-1, -1]

# Example usage:
sol = Solution()
print(sol.getPrimes(10))  # Output: [3, 7]
print(sol.getPrimes(3))   # Output: [-1, -1]
