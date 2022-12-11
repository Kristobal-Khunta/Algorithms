from collections import deque
from typing import List


DIRECTIONS: list[tuple] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
EMPTY: int = 2**31 - 1
GATE: int = 0


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        self.m = len(rooms)
        self.n = len(rooms[0])
        self.queue = deque()
        for row in range(self.m):
            for col in range(self.n):
                val = rooms[row][col]
                if val == GATE:
                    self.queue.append((row, col))
        self.bfs(self.queue, rooms)

    def bfs(self, queue, rooms: List[List[int]]) -> None:
        """
        find closest path to gate
        """
        while queue:
            row, col = queue.popleft()
            cur_val = rooms[row][col]
            for dr, dc in DIRECTIONS:
                next_row = row + dr
                next_col = col + dc
                if (
                    next_row < 0
                    or next_col < 0
                    or next_row >= self.m
                    or next_col >= self.n
                    or rooms[next_row][next_col] != EMPTY
                ):
                    continue

                rooms[next_row][next_col] = cur_val + 1
                self.queue.append((next_row, next_col))


from collections import deque
from typing import List


DIRECTIONS: list[tuple] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
EMPTY: int = 2**31 - 1
GATE: int = 0


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        self.m = len(rooms)
        self.n = len(rooms[0])
        self.queue = deque()
        for row in range(self.m):
            for col in range(self.n):
                val = rooms[row][col]
                if val == GATE:
                    self.queue.append((row, col))
        self.bfs(self.queue, rooms)

    def bfs(self, queue, rooms: List[List[int]]) -> None:
        """
        find closest path to gate
        """
        while queue:
            row, col = queue.popleft()
            cur_val = rooms[row][col]
            for dr, dc in DIRECTIONS:
                next_row = row + dr
                next_col = col + dc
                if (
                    next_row < 0
                    or next_col < 0
                    or next_row >= self.m
                    or next_col >= self.n
                    or rooms[next_row][next_col] != EMPTY
                ):
                    continue

                rooms[next_row][next_col] = cur_val + 1
                self.queue.append((next_row, next_col))


class Solution(object):
    """
    Space=> O(1)
    Time=> O(mn)
    """

    def numIslands(self, grid):
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    self.part_of_island(i, j, grid)
        return islands

    def part_of_island(self, i, j, grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != "1":
            return
        else:
            grid[i][j] = "0"
        self.part_of_island(i, j + 1, grid)
        self.part_of_island(i, j - 1, grid)
        self.part_of_island(i + 1, j, grid)
        self.part_of_island(i - 1, j, grid)
