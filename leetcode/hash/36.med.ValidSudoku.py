from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Time complexity: O(N^2)
        Space complexity: O(N^2)
        """
        seen_rows = defaultdict(set)
        seen_cols = defaultdict(set)
        seen_sbs = defaultdict(set)
        n_rows = len(board)
        n_cols = len(board[0])
        for i in range(n_rows):
            for j in range(n_cols):
                val = board[i][j]
                if val == ".":
                    continue
                sub_box = int(i / 3), int(j / 3)
                if (
                    (val in seen_rows[i])
                    or (val in seen_cols[j])
                    or (val in seen_sbs[sub_box])
                ):
                    return False
                seen_rows[i].add(val)
                seen_cols[j].add(val)
                seen_sbs[sub_box].add(val)
        return True
