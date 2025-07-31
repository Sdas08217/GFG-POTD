class Solution:
    def powerfulInteger(self, intervals, k):
        from collections import defaultdict

        # Step 1: Track the frequency changes using a difference array approach
        diff = defaultdict(int)

        for start, end in intervals:
            diff[start] += 1
            diff[end + 1] -= 1

        # Step 2: Sort the unique points where changes happen
        sorted_points = sorted(diff.keys())

        current_coverage = 0
        max_powerful = -1
        prev_point = None

        for point in sorted_points:
            if prev_point is not None and current_coverage >= k:
                # All integers between prev_point and point - 1 have >= k coverage
                max_powerful = max(max_powerful, point - 1)

            current_coverage += diff[point]
            prev_point = point

        return max_powerful
