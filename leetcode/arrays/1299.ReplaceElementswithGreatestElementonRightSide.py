class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = arr[-1]
        prev_max = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] >= max_val:
                prev_max = max_val
                max_val = arr[i]
                arr[i] = prev_max
            else:
                arr[i] = max_val
        arr[-1] = -1
        return arr


class Solution3:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], max_val = max_val, max(arr[i], max_val)
        return arr


class Solution3:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        prev_max = -1
        for i in range(len(arr) - 1, -1, -1):
            prev_max = max_val
            max_val = max(arr[i], max_val)
            arr[i] = prev_max
        return arr
