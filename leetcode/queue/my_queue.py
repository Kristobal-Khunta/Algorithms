class MyCircularQueue(object):
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """

        self.queue = [None for _ in range(k)]
        self.size = k
        self.cnt = 0
        self.tail = -1
        self.head = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.tail += 1
        if self.tail == self.size:
            self.tail = 0
        self.queue[self.tail] = value
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """

        if self.isEmpty():
            return False
        self.cnt -= 1
        self.queue[self.head] = None
        self.head += 1
        if self.head == self.size:
            self.head = 0
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> bool:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1

        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.cnt == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        """
        return self.cnt == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
