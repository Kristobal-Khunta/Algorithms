class MyCircularQueue(object):
    def __init__(self, k):
        """
        :type k: int
        """

        self.queue = [None for _ in range(k)]
        self.size = k
        self.cnt = 0
        self.tail = -1 
        self.head = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.tail += 1
        if self.tail == self.size:
            self.tail = 0
        self.queue[self.tail] = value
        self.cnt += 1
        return True

    def deQueue(self):
        """
        :rtype: bool
        """

        if self.isEmpty():
            return False
        self.cnt -= 1
        self.queue[self.head] = None
        self.head += 1
        if self.head == self.size:
            self.head = 0
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1

        return self.queue[self.tail]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.cnt == 0

    def isFull(self):
        """
        :rtype: bool
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
