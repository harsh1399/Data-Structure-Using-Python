class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self,data):
        if data == self.data:
            return
        if data > self.data:
            if self.right:
                self.right.add_node(data)
            else:
                self.right = BSTNode(data)
        else:
            if self.left:
                self.left.add_node(data)
            else:
                self.left = BSTNode(data)

    def in_order_traversal(self):
        if self is None:
            return
        if self.left:
            self.left.in_order_traversal()
        print(self.data,end=' ')
        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        if self is None:
            return
        print(self.data,end=' ')
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self is None:
            return
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.data, end=' ')

    def search(self,data):
        if self.data == data:
            return True
        if self.data > data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def delete_node(self,data):
        pass

    @staticmethod
    def build_tree(elements):
        root = BSTNode(elements[0])
        for i in range(1,len(elements)):
            root.add_node(elements[i])
        return root


if __name__ == '__main__':
    root = BSTNode(4)
    root.add_node(2)
    root.add_node(3)
    root.add_node(1)
    root.add_node(7)
    root.add_node(5)
    root.add_node(6)
    root.add_node(8)
    print('Inorder Traversal:')
    root.in_order_traversal()
    print('\nPreorder Traversal:')
    root.pre_order_traversal()
    print('\nPostorder Traversal:')
    root.post_order_traversal()
    is_present = root.search(8)
    print(f"\n{is_present}")