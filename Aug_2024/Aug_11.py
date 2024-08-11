# Job Sequencing Problem
class Solution:

    def JobScheduling(self, Jobs, n):

        sorted_Jobs = sorted(Jobs, key = lambda x: x.profit, reverse = True)
        timeline = [-1] * n
        sm_ct, ct = 0, 0

        for i in sorted_Jobs:
            idx = i.deadline - 1

            while idx >= 0 and timeline[idx] != -1: idx -= 1

            if idx >= 0:

                timeline[idx] = i.id
                sm_ct, ct = sm_ct + i.profit, ct + 1

        return [ct, sm_ct]

  # Example usage:
if __name__ == "__main__":
    Jobs = [Job(1, 4, 20), Job(2, 1, 10), Job(3, 1, 40), Job(4, 1, 30)]
    n = 4

    solution = Solution()
    result = solution.JobScheduling(Jobs, n)
    print(f"Number of jobs done: {result[0]}, Maximum profit: {result[1]}")
