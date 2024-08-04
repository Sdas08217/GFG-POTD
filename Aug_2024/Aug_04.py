# N meetings in one room
class Solution:
    def maximumMeetings(self, n, start, end):
        meetings = [[start[i], end[i]] for i in range(n)]
        meetings.sort(key=lambda x: x[1])

        count = 1
        last_end = meetings[0][1]

        for i in range(1, n):
            if meetings[i][0] > last_end:
                count += 1
                last_end = meetings[i][1]

        return count

  # Define the start and end times of the meetings
n = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

# Create an instance of the Solution class
solution = Solution()

# Call the maximumMeetings method and print the result
max_meetings = solution.maximumMeetings(n, start, end)
print(f"The maximum number of meetings that can be attended is: {max_meetings}")
