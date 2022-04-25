# Given an integer rowIndex, return the rowIndexth
#  (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of
#  the two numbers directly above it as shown:
# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]

from typing import List
class MyBadSolution:
    def calcVal(self, i, j):
        if j == 0 or i == j:
            return 1
        return self.calcVal(i - 1, j - 1) + self.calcVal(i - 1, j)

    def getRow(self, rowIndex: int) -> List[int]:

        a = []
        for colIndex in range(rowIndex + 1):
            res = self.calcVal(rowIndex, colIndex)
            a.append(res)
        return a


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        a = [
            1,
        ]
        prevRow = self.getRow(rowIndex - 1)
        print(prevRow)
        prev = prevRow[0]

        for idx in range(1, len(prevRow)):
            cur = prevRow[idx]
            a.append(prev + cur)
            prev = cur
        a.append(1)
        return a


class SolutionComments:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        if rowIndex == 0:
            return row
        prev_row = self.getRow(rowIndex - 1)
        for i in range(1, len(row) - 1):
            row[i] = prev_row[i - 1] + prev_row[i]
        return row
