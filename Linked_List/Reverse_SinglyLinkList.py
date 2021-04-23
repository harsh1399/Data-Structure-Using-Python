"""Given pointer to the head node of a linked list, the task is to reverse the linked list. """

from Linked_List import BasicOperations


def reverse_iterative(list1):
    prev = None
    temp = list1.head
    forward = temp.next
    while temp:
        temp.next = prev
        prev = temp
        temp = forward
        if forward:
            forward = forward.next
    list1.head = prev


def reverse_recursive(node, prev=None):
    if node is None:
        return prev
    forward = node.next
    node.next = prev
    return reverse_recursive(forward, node)


if __name__ == '__main__':
    link_list = BasicOperations.LinkedList()
    link_list.insert_values([4,3,2,0,6,8,7])
    print("Before Reversing:")
    link_list.display()
    reverse_iterative(link_list)
    print("After Reversing")
    link_list.display()
    print("After Reversing Recursively")
    link_list.head = reverse_recursive(link_list.head)
    link_list.display()