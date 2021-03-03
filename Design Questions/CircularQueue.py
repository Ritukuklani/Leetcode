class MyCircularQueue:
    """Circular Queue is also a linear data structure, which follows the principle 
    of FIFO(First In First Out), but instead of ending the queue at the last position, 
    it again starts from the first position after the last, hence making the queue behave 
    like a circular data structure."""
    def __init__(self, k: int):
        self.queue = [0]*k
        self.head = 0
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.size>=self.capacity:
            return False
        # print((self.head+self.size)%self.capacity)
        self.queue[(self.head+self.size)%self.capacity] = value
        self.size+=1
        return True

    def deQueue(self) -> bool:
        if self.size<=0:
            return False
        self.head = (self.head+1)%self.capacity
        self.size-=1
        return True

    def Front(self) -> int:
        if self.size<=0:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.size<=0:
            return -1
        return self.queue[(self.head+self.size-1)%self.capacity]

    def isEmpty(self) -> bool:
        return self.size<=0


    def isFull(self) -> bool:
        return self.size>=self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()