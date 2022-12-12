from typing import List


class Solution:
    def neighbors(self, code):
        for i in range(4):
            x = int(code[i])
            for diff in (-1, 1):
                y = (x + diff + 10) % 10
                yield code[:i] + str(y) + code[i + 1 :]

    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        n_steps = 0
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0
        queue = collections.deque()
        queue.append("0000")
        visited.add("0000")
        while queue:
            n_steps += 1
            for _ in range(len(queue)):
                code = queue.popleft()
                for n in self.neighbors(code):
                    if n == target:
                        return n_steps
                    if (n in visited) or (n in deadends):
                        continue
                    queue.append(n)
                    visited.add(n)

        return -1
