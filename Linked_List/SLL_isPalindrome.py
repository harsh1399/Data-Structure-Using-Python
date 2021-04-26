"""Given the head of a singly linked list, return true if it is a palindrome."""

from Linked_List import BasicOperations


def is_palindrome(list1):
    middle = list1.head
    fast =  list1.head
    current = list1.head
    prev = None
    while fast and fast.next:
        middle = middle.next
        fast = fast.next.next
        current.next = prev
        prev = current
        current = middle

    if fast:
        current = current.next
    while prev and current:
        if prev.data != current.data:
            return False
        prev = prev.next
        current = current.next
    else:
        return True


if __name__ == '__main__':
    list1 = BasicOperations.LinkedList()
    list1.insert_values([1,2,3,4,4,3,2,1])
    print(is_palindrome(list1))
