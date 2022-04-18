from typing import List


class Solution1:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_idx = 0
        max_val = arr[0]
        for i, val in enumerate(arr):
            if val > max_val:
                max_val = val
                max_idx = i
        if (max_idx == 0) or (max_idx == len(arr) - 1):
            return False
        for i in range(0, max_idx):
            if arr[i] >= arr[i + 1]:
                return False
        for i in range(max_idx, len(arr) - 1):
            if arr[i] <= arr[i + 1]:
                return False
        return True


class Solution2:
    # идея идем на встречу друг другу, если в 1 индекс - то все ок
    # https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/discuss/1717377/JavaC++Python-EASY-to-go-through-solution-and-EXPLANATION
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        l = 0
        r = len(arr) - 1
        while l + 1 < len(arr) - 1 and arr[l] < arr[l + 1]:
            l += 1
        while r - 1 > 0 and arr[r] < arr[r - 1]:
            r -= 1
        return l == r


class Solution3(object):

    # Algorithm
    # Let's walk up from left to right until we can't:
    #  that has to be the peak. We should ensure the peak
    #  is not the first or last element.
    # Then, we walk down. If we reach the end,
    #  the array is valid, otherwise its not.
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N - 1:
            return False

        # walk down
        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1
