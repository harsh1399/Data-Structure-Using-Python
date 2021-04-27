"""You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list."""

from Linked_List import BasicOperations

head = None


def insert(data):
    global head
    new_node = BasicOperations.Node(data)
    if head is None:
        head = new_node
    else:
        new_node.next = head
        head = new_node


def add_same_size_list(head1, head2):
    if head1 is None:
        return 0
    addition = head1.data + head2.data + add_same_size_list(head1.next, head2.next)
    carry = addition // 10
    data = addition % 10
    insert(data)
    return carry


def add2numbers(head1, head2):
    count1 = 0
    temp = head1
    while temp:
        count1 += 1
        temp = temp.next
    count2 = 0
    temp = head2
    while temp:
        count2 += 1
        temp = temp.next
    carry = 0
    if count1 == count2:
        carry = add_same_size_list(head1, head2)
    else:
        if count2 < count1:
            while count2 - count1 != 0:
                new_node = BasicOperations.Node(0)
                new_node.next = head2
                head2 = new_node
                count2 += 1
        else:
            while count1 - count2 != 0:
                new_node = BasicOperations.Node(0)
                new_node.next = head1
                head1 = new_node
                count1 += 1
        carry = add_same_size_list(head1, head2)
    if carry != 0:
        global head
        new_node = BasicOperations.Node(carry)
        new_node.next = head
        head = new_node


if __name__ == '__main__':
    list1 = BasicOperations.LinkedList()
    list1.insert_values([7,2,4,3])
    list2 = BasicOperations.LinkedList()
    list2.insert_values([5,6,4])
    add2numbers(list1.head,list2.head)
    list3 = BasicOperations.LinkedList()
    list3.head = head
    list3.display()
