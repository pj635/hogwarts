class BinaryTree():
    def __init__(self):
        self.tree = None

    class Node():
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def insert(self, ele):
        node = self.Node(ele)
        if self.tree is None:
            self.tree = node
            return True
        p = self.tree
        while p is not None:
            if ele == p.data:
                break
            elif ele < p.data:
                if p.left is None:
                    p.left = node
                p = p.left
            else:
                if p.right is None:
                    p.right = node
                p = p.right
        return True

    def find(self, ele):
        p = self.tree
        while p is not None:
            if ele == p.data:
                return p
            elif ele < p.data:
                p = p.left
            else:
                p = p.right
        return None

    def mid_order(self, node:Node):
        if node is None:
            return
        self.mid_order(node.left)
        print(node.data)
        self.mid_order(node.right)

    def delete(self, ele):
        p = self.tree
        pp = None

        while p is not None:
            if ele == p.data:
                break
            elif ele < p.data:
                pp = p
                p = p.left
            else:
                pp = p
                p = p.right
        if p is None:
            return False

        child = None
        if p.left is not None and p.right is not None:
            tmp_p = p.right
            tmp_pp = pp
            while tmp_p.left is not None:
                tmp_pp = tmp_p
                tmp_p = tmp_p.left
            p.data = tmp_p.data
            p = tmp_p
            pp = tmp_pp

        elif p.left is None and p.right is None:
            child = None
        elif p.right is not None:
            child = p.right
        elif p.left is not None:
            child = p.left

        if pp.left == p:
            pp.left = child
        else:
            pp.right = child
        return True


def test1():
    tree = BinaryTree()
    tree.insert(20)
    tree.insert(50)
    tree.insert(10)
    tree.insert(40)
    tree.insert(30)

    print(tree.find(20).data)
    assert tree.find(25) is None
    tree.mid_order(tree.tree)

    tree.delete(20)
    print("*" * 100)
    tree.mid_order(tree.tree)
