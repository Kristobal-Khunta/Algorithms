class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(1) - we have a limited number of chars
        """
        if len(s) != len(t):
            return False
        counter = {}
        for idx in range(len(s)):
            val_s = s[idx]
            val_t = t[idx]
            if val_s not in counter:
                counter[val_s] = 0
            if val_t not in counter:
                counter[val_t] = 0

            counter[val_s] += 1
            counter[val_t] -= 1

        for val in counter.values():
            if val != 0:
                return False
        return True
