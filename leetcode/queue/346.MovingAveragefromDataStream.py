from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.queue = [0] * size
        self.idx = -1  # can lead to integer overflow
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.idx += 1
        insert_idx = self.idx % self.size
        self.sum -= self.queue[insert_idx]
        self.queue[insert_idx] = val
        self.sum += val
        demom = self.size if self.idx >= self.size else self.idx + 1
        return self.sum / demom


class MovingAverageDeque:
    def __init__(self, size: int):
        self.queue = deque()
        self.sum = 0
        self.size = size 

    def next(self, val: int) -> float:
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.sum -= self.queue.popleft()
        self.sum += val
        return self.sum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
