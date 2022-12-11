from collections import deque
from typing import List

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.num_islands = 0
        self.m = len(grid)
        self.n = len(grid[0])
        for x in range(self.m):
            for y in range(self.n):
                val = grid[x][y]
                if val != "1":
                    continue
                self.num_islands += 1
                self.bfs(x, y, grid)
        return self.num_islands

    def bfs(self, x: int, y: int, grid: List[List[str]]):
        queue = deque()
        queue.append((x, y))
        grid[x][y] = "0"

        while queue:
            x_cur, y_cur = queue.popleft()
            for dx, dy in DIRECTIONS:
                nx = x_cur + dx
                ny = y_cur + dy
                if (nx < 0) or (nx >= self.m) or (ny < 0) or (ny >= self.n):
                    continue
                val = grid[nx][ny]
                if val != "1":
                    continue
                queue.append((nx, ny))
                grid[nx][ny] = "0"
