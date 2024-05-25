# You and your books
class Solution:
    # Your task is to complete this function
    # Function should return an integer
    # a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
        max_books = 0
        current_books = 0
        left = 0
        
        for right in range(n):
            if arr[right] <= k:
                current_books += arr[right]
                max_books = max(max_books, current_books)
            else:
                current_books = 0
                left = right + 1
        
        return max_books

# Example usage
if __name__ == '__main__':
    # Example 1
    n1 = 8
    k1 = 1
    arr1 = [3, 2, 2, 3, 1, 1, 1, 3]
    ob1 = Solution()
    print(ob1.max_Books(n1, k1, arr1))  # Output: 3

    # Example 2
    n2 = 8
    k2 = 2
    arr2 = [3, 2, 2, 3, 1, 1, 1, 3]
    ob2 = Solution()
    print(ob2.max_Books(n2, k2, arr2))  # Output: 4
