# TASK
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
#  and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left_pointer = m - 1
        right_pointer = n - 1
        write_pointer = m + n - 1
        # мы записываем в левый массив
        # когда закончился правый массив левый уже лежит отсортированный
        while right_pointer >= 0:
            # проверяем чтобы левый указатель не ушел за границу
            if left_pointer >= 0 and nums1[left_pointer] >= nums2[right_pointer]:
                nums1[write_pointer] = nums1[left_pointer]
                left_pointer -= 1
            else:
                nums1[write_pointer] = nums2[right_pointer]
                right_pointer -= 1
            write_pointer -= 1

# следим чтобы 2 указателя не ушли за границы
# сначала проверяем m затем n
# если закончился указатель m - процесс завершен
# если закончился указатель n - значит мы должны скопировать оставшийся n в начало общего
def merge(self, nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]
