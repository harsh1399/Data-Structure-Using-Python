"""Given head, the head of a linked list, determine if the linked list has a cycle in it."""


from Linked_List import BasicOperations


def has_cycle(list1):                # floyd cycle detection algorithm
    if list1.head is None:
        return False
    if list1.head.next is None:
        return False
    slow = list1.head
    fast = list1.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    else:
        return False


def cycle(list1):           # Another method to find cycle
    temp = list1.head
    if list1.head is None:
        return False
    if list1.head.next is None:
        return False
    while temp:
        temp.data = None
        temp = temp.next
        if temp.data is None:
            return True
    return False


if __name__ == '__main__':
    list1 = BasicOperations.LinkedList()
    new_node = BasicOperations.Node(3)
    list1.head = new_node
    new_node = BasicOperations.Node(4)
    list1.head.next = new_node
    new_node = BasicOperations.Node(5)
    list1.head.next.next = new_node
    new_node = BasicOperations.Node(6)
    list1.head.next.next.next = new_node
    new_node = BasicOperations.Node(7)
    list1.head.next.next.next.next = list1.head.next
    print(cycle(list1))
