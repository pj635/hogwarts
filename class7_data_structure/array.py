class Array():
    def __init__(self, capacity):
        self.data = [-1] * capacity
        self.count = 0
        self.capacity = capacity

    def insert(self, location, val):
        if self.count == self.capacity:
            return False
        if location < 0 or location > self.count:
            return False

        for i in range(self.count, location, -1):
            self.data[i] = self.data[i - 1]
        self.data[location] = val
        self.count += 1
        return True

    def find(self, location):
        if location < 0 or location > self.count - 1:
            return None
        return self.data[location]

    def delete(self, location):
        if location < 0 or location > self.count - 1:
            return False

        for i in range(location, self.count - 1) :
            self.data[i] = self.data[i + 1]
        self.count -= 1
        return True


def test_demo():
    array = Array(5)
    array.insert(0, 1)
    array.insert(0, 2)
    array.insert(1, 3)
    array.insert(2, 4)
    array.insert(4, 5)

    # 判断插入不成功
    assert not array.insert(0, 100)
    assert array.find(0) == 2
    assert array.find(2) == 4
    assert array.find(4) == 5
    assert array.find(10) == None
    assert array.count == 5
    removed = array.delete(4)
    assert removed
    assert array.find(4) == None
    removed = array.delete(10)
    assert not removed
    # 2 3 4 1 5
    assert array.data == [2, 3, 4, 1, 5]


if __name__ == '__main__':
    test_demo()
