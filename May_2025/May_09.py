class Solution:
    def findMaximumNum(self, s, k):
        s_list = list(s)
        max_str = [''.join(s_list)]  # Use a list to allow modification in nested function
        
        def backtrack(current, pos, swaps_left):
            if swaps_left == 0 or pos == len(current):
                return
            # Find the maximum digit from current pos to end
            max_digit = max(current[pos:], default='')
            # Iterate from the end to find the rightmost occurrence first
            for j in range(len(current)-1, pos-1, -1):
                if current[j] == max_digit:
                    if j == pos:
                        # No swap needed, move to next position
                        backtrack(current, pos + 1, swaps_left)
                    else:
                        # Create a new list with the swap
                        new_current = current.copy()
                        new_current[pos], new_current[j] = new_current[j], new_current[pos]
                        # Update the maximum if this new configuration is better
                        current_str = ''.join(new_current)
                        if current_str > max_str[0]:
                            max_str[0] = current_str
                        # Proceed with the next position and decrement swaps
                        backtrack(new_current, pos + 1, swaps_left - 1)
        
        backtrack(s_list, 0, k)
        return max_str[0]
