# Construct list using given q XOR queries
from typing import List

class Solution:
    def constructList(self, q: int, queries: List[List[int]]) -> List[int]:
        s = [0]  # Initial list containing only 0
        cumulative_xor = 0  # Keep track of the cumulative XOR value

        for query in queries:
            if query[0] == 0:
                x = query[1]
                s.append(x ^ cumulative_xor)  # Insert x with current cumulative XOR
            elif query[0] == 1:
                x = query[1]
                cumulative_xor ^= x  # Update cumulative XOR value

        # Apply the cumulative XOR to all elements before returning the result
        s = [a ^ cumulative_xor for a in s]
        s.sort()  # Sort the final list before returning
        return s
# Example usage
if __name__ == "__main__":
    # Test case 1
    q1 = 5
    queries1 = [[0, 6], [0, 3], [0, 2], [1, 4], [1, 5]]
    obj1 = Solution()
    result1 = obj1.constructList(q1, queries1)
    print(result1)  # Expected output: [1, 2, 3, 7]

    # Test case 2
    q2 = 3
    queries2 = [[0, 2], [1, 3], [0, 5]]
    obj2 = Solution()
    result2 = obj2.constructList(q2, queries2)
    print(result2)  # Expected output: [1, 3, 5]
