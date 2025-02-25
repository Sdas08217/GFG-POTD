class Solution:
    def getMaxArea(self, arr):
        n = len(arr)
        max_area = 0
        stack = []
        i = 0
        
        # Process all bars in the histogram.
        while i < n:
            # If stack is empty or current bar is higher than the bar at stack top, push index.
            if not stack or arr[i] >= arr[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                # Pop the top index from the stack and calculate the area.
                top = stack.pop()
                if not stack:
                    area = arr[top] * i
                else:
                    area = arr[top] * (i - stack[-1] - 1)
                max_area = max(max_area, area)
        
        # Process the remaining indices in the stack.
        while stack:
            top = stack.pop()
            if not stack:
                area = arr[top] * n
            else:
                area = arr[top] * (n - stack[-1] - 1)
            max_area = max(max_area, area)
        
        return max_area
