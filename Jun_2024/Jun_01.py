# Odd Even Problem
class Solution:
    def oddEven(self, s: str) -> str:
        # Initialize frequency dictionary
        freq = {}
        
        # Count frequency of each character in the string
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        # Initialize counts for x and y
        x = 0
        y = 0
        
        # Iterate through the frequency dictionary
        for char, count in freq.items():
            position = ord(char) - ord('a') + 1  # Calculate the position in the alphabet
            if position % 2 == 0:  # Even position
                if count % 2 == 0:  # Even frequency
                    x += 1
            else:  # Odd position
                if count % 2 != 0:  # Odd frequency
                    y += 1
        
        # Check if the sum of x and y is even or odd
        if (x + y) % 2 == 0:
            return "EVEN"
        else:
            return "ODD"
# Example usage:
if __name__ == "__main__":
    test_cases = [
        "abbbcc",   # Expected output: "ODD"
        "nobitaa",  # Expected output: "EVEN"
        "aaaabbbbccccc",  # Expected output: "EVEN"
        "abcdefghijk",    # Expected output: "ODD"
    ]
    
    obj = Solution()
    for s in test_cases:
        result = obj.oddEven(s)
        print(f"Input: {s}, Output: {result}")
