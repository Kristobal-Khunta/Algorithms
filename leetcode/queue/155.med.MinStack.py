class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        cur_min = self.stack[-1][1]
        self.stack.append((val, min(val, cur_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# great explanation of different approaches:
# https://leetcode.com/problems/min-stack/solutions/514932/official-solution/
# Approach 1: Stack of Value/ Minimum Pairs
# Approach 2: Two Stacks
# Approach 3: Improved Two Stacks
