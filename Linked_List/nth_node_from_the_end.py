""" Program for n’th node from the end of a Linked List """

from Linked_List import BasicOperations


def nth_from_the_end(list1,n):
    fast = list1.head
    slow = list1.head
    for i in range(n-1):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    return slow


def middle_node(list1):
    fast = list1.head
    slow = list1.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


if __name__ == '__main__':
    list1 = BasicOperations.LinkedList()
    list1.insert_values([1,2,3,4,5,6,7])
    nth_node = nth_from_the_end(list1,3)
    print("3rd node from the list")
    print(nth_node.data)
    print("Middle of the list")
    middle = middle_node(list1)
    print(middle.data)