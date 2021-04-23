"""Given a linked list, reverse the nodes of a linked list k at a time and return its modified list"""

from Linked_List import BasicOperations


def reverse_k_nodes(head, k):
    prev = None
    current = head
    forward = None
    count = 0
    while count < k and current is not None:
        forward = current.next
        current.next = prev
        prev = current
        current = forward
        count += 1
    if current is not None:
        head.next = reverse_k_nodes(current, k)
    return prev


if __name__ == '__main__':
    link_list = BasicOperations.LinkedList()
    link_list.insert_values([4,2,8,3,1,7,5,6])
    link_list.display()
    print("After reversing K nodes at a time")
    link_list.head = reverse_k_nodes(link_list.head, 3)
    link_list.display()