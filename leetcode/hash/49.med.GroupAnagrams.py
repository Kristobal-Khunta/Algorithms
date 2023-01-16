from typing import List
from collections import defaultdict


class Solution:
    """
    Time Complexity: O(N*Klog(K)), where N is the length of strs,
                    and K is the maximum length of a string in strs
    Space Complexity: O(NK)
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}  # "sorted_str: list_of_strs"
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word not in hashmap:
                hashmap[sorted_word] = []
            hashmap[sorted_word].append(word)
        return [x for x in hashmap.values()]


class SolutionNeetcode:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
