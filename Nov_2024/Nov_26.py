# Max Circular Subarray Sum.
def circularSubarraySum(arr):
    n = len(arr)
    
    # Helper function to compute the maximum subarray sum using Kadane's algorithm
    def kadane(nums):
        max_ending_here = max_so_far = nums[0]
        for num in nums[1:]:
            max_ending_here = max(num, max_ending_here + num)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    
    # Step 1: Compute the standard maximum subarray sum
    max_kadane = kadane(arr)
    
    # Step 2: Compute the maximum circular subarray sum
    total_sum = sum(arr)
    
    # Inverting the array to find the minimum subarray sum
    # This is effectively `total_sum - min_subarray_sum`
    min_ending_here = min_so_far = arr[0]
    for i in range(1, n):
        min_ending_here = min(arr[i], min_ending_here + arr[i])
        min_so_far = min(min_so_far, min_ending_here)
    
    max_circular = total_sum - min_so_far  # Circular sum
    
    # Step 3: Handle the edge case where all numbers are negative
    # In this case, `max_circular` will be 0, so we return `max_kadane`
    if max_circular == 0:
        return max_kadane
    
    # Step 4: Return the maximum of standard and circular sums
    return max(max_kadane, max_circular)
Key Optimizations:
