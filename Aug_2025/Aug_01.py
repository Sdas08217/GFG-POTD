from collections import defaultdict

class Solution:
    def countBalanced(self, arr):
        vowels = set('aeiou')
        
        balance = 0
        count = 0
        freq = defaultdict(int)
        freq[0] = 1  # Starting neutral balance
        
        for s in arr:
            for ch in s:
                if ch in vowels:
                    balance += 1
                else:
                    balance -= 1
            count += freq[balance]
            freq[balance] += 1
        
        return count
