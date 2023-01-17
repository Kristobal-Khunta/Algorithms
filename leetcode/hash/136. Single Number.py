class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        optimal with bit manipulation -  T: O(n), S: O(1)
        """
        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 0
            hashmap[n] += 1
            if hashmap[n] == 2:
                del hashmap[n]
        return list(hashmap.keys())[0]
