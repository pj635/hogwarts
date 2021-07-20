class Queue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [-1] * capacity
        self.tail = 0
        self.head = 0

    def dequeue(self):
        if self.head == self.tail:
            return None
        ele = self.data[self.head]
        self.head = (self.head + 1) % self.capacity
        return ele

    def enqueue(self, ele):
        if (self.tail + 1) % self.capacity == self.head:
            return False
        self.data[self.tail] = ele
        self.tail = (self.tail + 1) % self.capacity
        return True

def test():
    queue = Queue(3)
    queue.enqueue(100)
    queue.enqueue(200)
    assert queue.enqueue(3) == False
    assert queue.dequeue() == 100
    assert queue.dequeue() == 200
    assert queue.dequeue() == None

