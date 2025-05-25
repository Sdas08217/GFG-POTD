class Solution:
    def pythagoreanTriplet(self, arr):
        n = len(arr)
        # Step 1: Square all elements
        squares = [x * x for x in arr]
        # Step 2: Use set for O(1) average-time lookups
        square_set = set(squares)
        
        # Step 3: Try all pairs (a, b) and check if a² + b² is in the set
        for i in range(n):
            for j in range(i + 1, n):
                if squares[i] + squares[j] in square_set:
                    return True
        return False
