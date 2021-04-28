"""Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. """


class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.down = None


def merge(node1, node2):
    merge_head = None
    if node1.data > node2.data:
        merge_head = node2
        node2 = node2.down
    else:
        merge_head = node1
        node1 = node1.down
    temp = merge_head
    while node1 and node2:
        if node1.data > node2.data:
            temp.down = node2
            temp = temp.down
            node2 = node2.down
        else:
            temp.down = node1
            temp = temp.down
            node1 = node1.down
    if node1:
        temp.down = node1
    if node2:
        temp.down = node2
    return merge_head


def flatten(node):
    if node is None or node.right is None:
        return node
    node.right = flatten(node.right)
    merge_head = merge(node,node.right)
    return merge_head


if __name__ == '__main__':
    head = Node(1)
    head.right = Node(2)
    head.right.right = Node(3)
    head.right.right = Node(4)
    head.down = Node(5)
    head.down.down = Node(6)
    head.right.right.down = Node(7)
    head.right.right.down.down = Node(8)
    head.right.right.down.down.down = Node(9)
    flatten_head = flatten(head)
    temp = flatten_head
    while temp:
        print(temp.data,'->',end='',sep='')
        temp = temp.down
    print("Null")
