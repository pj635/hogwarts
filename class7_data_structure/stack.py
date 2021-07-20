class ArrayStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = 0
        self.data = [-1] * capacity

    def push(self, ele):
        if self.top == self.capacity:
            return False
        self.data[self.top] = ele
        self.top += 1
        return True

    def pop(self):
        if self.top == 0:
            return None
        ele = self.data[self.top - 1]
        self.top -= 1
        return ele

def test():
    stack = ArrayStack(3)
    stack.push(100)
    stack.push(200)
    stack.push(300)
    assert stack.push(400) == False

    assert stack.pop() == 300
    assert stack.pop() == 200
    assert stack.pop() == 100
    assert stack.pop() == None



class StackBasedOnLinkedList:
    def __init__(self):
        self.top = None

    def push(self, ele):
        node = self.Node(ele)
        node.next = self.top
        self.top = node
        return True
    def pop(self):
        if self.top == None:
            return None
        ele = self.top.ele
        self.top = self.top.next
        return ele

    class Node:
        def __init__(self, ele):
            self.ele = ele
            self.next = None


def test_StackBasedOnLinkedList():
    stack = StackBasedOnLinkedList()
    stack.push(100)
    stack.push(200)
    stack.push(300)
    assert stack.pop() == 300
    assert stack.pop() == 200
    assert stack.pop() == 100
    assert stack.pop() == None