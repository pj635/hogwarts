class List():
    def __init__(self):
        self.head = None

    class Node():
        def __init__(self, ele):
            self.next = None
            self.ele = ele

    def insert_to_head(self, ele):
        node = self.Node(ele)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def insert_to_tail(self, ele):
        node = self.Node(ele)
        p = self.head
        if p is None:
            self.head = node
            return
        while p.next is not None:
            p = p.next
        p.next = node

    def insert_before(self, node, ele):
        if node == None:
            return False
        p = self.head
        new_node = self.Node(ele)
        if p == node:
            new_node.next = self.head
            self.head = new_node
            return True
        while p.next != node and p is not None:
            p = p.next
        if p is None:
            return  False
        new_node.next = p.next
        p.next = new_node
        return True

    def insert_after(self, node, ele):
        p = self.head
        new_node = self.Node(ele)
        if node is None:
            new_node.next = self.head
            self.head = new_node
        while p is not None and p != node:
            p = p.next
        if p is None:
            return False
        new_node.next = p.next
        p.next = new_node
        return True


    def delete(self, ele):
        p = self.head
        q = None
        while p is not None and p.ele != ele:
            q = p
            p = p.next
        if p == None:  #链表中没有要删除的元素
            return False
        elif q == None:  #要删除的元素在头节点
            self.head = self.head.next
        else: #要删除的元素存在与链表中切不在头节点
            q.next = p.next
        return True

    def find(self, ele) -> Node:
        p = self.head
        while p is not None and p.ele != ele:
            p = p.next
        if p is None:
            return None
        return p
    def get_list(self):
        l = []
        p = self.head
        while p is not None:
            l.append(p.ele)
            p = p.next
        return l


def test1():
    l = List()
    l.insert_to_tail(100)
    l.insert_to_tail(200)
    l.insert_to_tail(300)
    l.insert_to_head(50)
    print(l.get_list())
    l.delete(50)
    assert l.find(100).ele == 100
    assert l.find(200).ele == 200
    assert l.find(300).ele == 300
    l.delete(100)
    print(l.get_list())
    l.delete(300)
    print(l.get_list())
    l.delete(200)
    print(l.get_list())

def test2():
    l = List()
    l.insert_to_tail(100)
    l.insert_to_tail(200)
    l.insert_to_tail(300)
    l.insert_to_head(50)
    assert l.insert_before(None, 10) == False
    node = l.find(50)
    print(node.ele)
    assert l.insert_before(node, 10)
    assert l.get_list() == [10, 50, 100, 200, 300]
    print(l.get_list())
    l.insert_after(None, 1)
    assert l.get_list() == [1, 10, 50, 100, 200, 300]
    print(l.get_list())
    node = l.find(1)
    l.insert_after(node, -100)
    assert l.get_list() == [1, -100, 10, 50, 100, 200, 300]
    print(l.get_list())
