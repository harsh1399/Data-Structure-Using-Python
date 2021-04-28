"""Given the head of a singly linked list, group all the nodes with
odd indices together followed by the nodes with even indices, and return the reordered list."""


from Linked_List import BasicOperations


def odd_even_list(head):
    if head is None or head.next is None:
        return head
    temp = head.next.next
    prev = head.next
    odd = head
    even = head.next
    count = 3
    while temp:
        if count % 2 != 0:
            prev.next = temp.next
            temp.next = even
            odd.next = temp
            odd = odd.next
            temp = prev.next
            count += 1
        else:
            prev = temp
            temp = temp.next
            count += 1
    return head


if __name__ == '__main__':
    list1 = BasicOperations.LinkedList()
    list1.insert_values([1,2,3,4,5,6,7])
    list1.head = odd_even_list(list1.head)
    list1.display()