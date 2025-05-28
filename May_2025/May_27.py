class Solution:
    def __init__(self):
        self.index = 0
        self.n = 0
        self.leaves = []

    def leafNodes(self, preorder):
        self.index = 0
        self.n = len(preorder)
        self.leaves = []
        self._findLeaves(preorder, float('-inf'), float('inf'))
        return self.leaves

    def _findLeaves(self, preorder, min_val, max_val):
        if self.index >= self.n:
            return

        val = preorder[self.index]
        if not (min_val < val < max_val):
            return

        self.index += 1
        left_index = self.index
        self._findLeaves(preorder, min_val, val)
        right_index = self.index
        self._findLeaves(preorder, val, max_val)

        # If no child was added after left/right, it's a leaf
        if left_index == right_index == self.index:
            self.leaves.append(val)
