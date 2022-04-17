class Solution1:
    # solution 2 https://leetcode.com/problems/duplicate-zeros/discuss/322576/Python-3-real-in-place-solution

    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # можно проверять через if длину массива и записывать
        # count zeros in array
        # equal num_zeros = arr.count(0)
        num_zeros = 0
        for num in arr:
            if num == 0:
                num_zeros += 1
        # нужно вернуть обрезанный массив
        # идем с конца
        N = len(arr)
        for i in range(N - 1, -1, -1):
            if i + num_zeros <= N - 1:
                arr[i + num_zeros] = arr[i]
            if arr[i] == 0:
                num_zeros -= 1
                if i + num_zeros <= N - 1:
                    arr[i + num_zeros] = 0
#https://leetcode.com/problems/merge-sorted-array/discuss/1176400/Best-Python-Solution-Faster-Than-99-One-Loop-No-Splicing-No-Special-Case-Loop

class Solution2:
    # solution 1 https://leetcode.com/problems/duplicate-zeros/solution/

    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included
                if left == length_ - possible_dups:
                    arr[
                        length_
                    ] = 0  # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
