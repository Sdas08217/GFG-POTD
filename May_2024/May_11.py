# Juggler Sequence

class Solution:
    def jugglerSequence(self, n):
     sequence = [n]
     while n != 1:
        if n % 2 == 0:
            n = int(n ** 0.5)
        else:
            n = int(n ** 1.5)
        sequence.append(n)
     return sequence

# Example usage
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()

    # Test case
    n = 5

    # Generate the Juggler sequence
    result = solution.jugglerSequence(n)

    # Print the Juggler sequence
    print("Juggler sequence starting from", n, ":", result)
