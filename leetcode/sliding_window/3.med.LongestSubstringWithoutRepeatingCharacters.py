class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
 
        left_idx = -1
        seen = {}
        longest = 0
        for idx, symb in enumerate(s):
            if symb in seen:
                left_idx = max(left_idx, seen[symb])
            longest = max(longest, idx - left_idx)
            seen[symb] = idx

        return longest
                
