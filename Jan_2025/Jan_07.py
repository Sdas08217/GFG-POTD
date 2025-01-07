class Solution:
    def countPairs(self, arr, target):
        # Initialize pointers and counter
        left = 0
        right = len(arr) - 1
        count = 0
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                # Count pairs with the same values at `left` and `right`
                if arr[left] == arr[right]:
                    num_elements = right - left + 1
                    count += (num_elements * (num_elements - 1)) // 2
                    break
                else:
                    left_count = 1
                    right_count = 1
                    # Count duplicates for `left`
                    while left + 1 < right and arr[left] == arr[left + 1]:
                        left += 1
                        left_count += 1
                    # Count duplicates for `right`
                    while right - 1 > left and arr[right] == arr[right - 1]:
                        right -= 1
                        right_count += 1
                    # Add combinations
                    count += left_count * right_count
                    # Move pointers inward
                    left += 1
                    right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return count
