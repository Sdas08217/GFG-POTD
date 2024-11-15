# Nearly sorted.
import heapq
class Solution:
    def nearlySorted(self, arr, k):
        # Initialize a min-heap with the first k+1 elements
        heap = arr[:k + 1]
        heapq.heapify(heap)
        
        index = 0
        
        # Process the remaining elements in arr
        for i in range(k + 1, len(arr)):
            arr[index] = heapq.heappop(heap)
            heapq.heappush(heap, arr[i])
            index += 1
        
        # Extract the remaining elements from the heap
        while heap:
            arr[index] = heapq.heappop(heap)
            index += 1


# Example usage
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Define the input array and value of k
    arr = [6, 5, 3, 2, 8, 10, 9]
    k = 3
    
    # Call the nearlySorted function
    solution.nearlySorted(arr, k)
    
    # Print the sorted array
    print("Sorted array:", arr)
