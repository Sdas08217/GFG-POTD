class Solution:
    def subarrayXor(self, arr, k):
        xor_map = {}
        prefixXor = 0
        count = 0
        for num in arr:
            # Update prefix XOR
            prefixXor ^= num
            
            # If the current prefix XOR equals k, it forms a valid subarray
            if prefixXor == k:
                count += 1
            # Check if there's a prefix that satisfies the condition
            if prefixXor ^ k in xor_map:
                count += xor_map[prefixXor ^ k]
            
            # Update the hashmap with the current prefix XOR
            xor_map[prefixXor] = xor_map.get(prefixXor, 0) + 1
        return count
