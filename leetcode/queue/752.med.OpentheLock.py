from typing import List
import collections


class Solution:
    """
    Space: O(A^N+D) for the queue and the set dead.

    time: O(N^2*A^N+D)
    a- number of digits in alphabet
    N - nuber of digits in lock
    D - size of deadends
    We might visit every lock combination, plus we need to instantiate our set dead. When we visit every lock combination, we spend O(N^2) time enumerating through and constructing each node.
    """

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


class Solution(object):
    def openLock(self, deadends, target):
        def neighbors(node):
            for i in xrange(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i + 1 :]

        dead = set(deadends)
        queue = collections.deque([("0000", 0)])
        seen = {"0000"}
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in dead:
                continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))
        return -1
