class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        return list(set(a)&set(b))
