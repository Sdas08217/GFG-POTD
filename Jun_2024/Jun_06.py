# Max sum in the configuration
def max_sum(a, n):
    # Calculate the initial sum S_0 and the sum of all elements in the array
    S_0 = sum(i * a[i] for i in range(n))
    sum_a = sum(a)
    
    # Initialize the maximum sum as the initial sum S_0
    max_sum = S_0
    current_sum = S_0
    
    # Iterate over the array to compute the sum for each rotation
    for k in range(1, n):
        current_sum = current_sum + sum_a - n * a[n - k]
        max_sum = max(max_sum, current_sum)
    
    return max_sum
# Example usage:
n1 = 4
a1 = [8, 3, 1, 2]
print(max_sum(a1, n1))  # Output: 29

n2 = 3
a2 = [1, 2, 3]
print(max_sum(a2, n2))  # Output: 8
