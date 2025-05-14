class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'

        # Start with the first row
        current = '1'
        for _ in range(1, n):
            next_row = ''
            count = 1
            # Iterate through the current row
            for j in range(1, len(current)): 
                if current[j] == current[j - 1]:
                    count += 1
                else:
                    # Append the count and the digit to the next row
                    next_row += str(count) + current[j - 1]
                    count = 1
            # Append the last counted group
            next_row += str(count) + current[-1]
            current = next_row

        return current
