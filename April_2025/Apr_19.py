class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def insert(self, root, num):
        node = root
        for i in range(31, -1, -1):  # 32-bit representation
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def findMaxXOR(self, root, num):
        node = root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit
            if toggled_bit in node.children:
                max_xor |= (1 << i)
                node = node.children[toggled_bit]
            else:
                node = node.children.get(bit, node)
        return max_xor

    def maxXor(self, arr):
        root = TrieNode()
        max_result = 0
        for num in arr:
            self.insert(root, num)
        for num in arr:
            max_result = max(max_result, self.findMaxXOR(root, num))
        return max_result
