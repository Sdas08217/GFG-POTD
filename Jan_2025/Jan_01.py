class Solution:
    def anagrams(self, arr):
        from collections import defaultdict
        # Dictionary to group anagrams
        anagram_groups = defaultdict(list)
        # Iterate over each word in the array
        for word in arr:
            # Sort the characters of the word to create a key
            key = ''.join(sorted(word))
            # Append the word to the corresponding group
            anagram_groups[key].append(word)
        # Return the grouped anagrams as a list of lists
        return list(anagram_groups.values())
