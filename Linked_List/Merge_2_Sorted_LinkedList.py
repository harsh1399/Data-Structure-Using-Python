'''
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.
'''
from Linked_List import BasicOperations


def merge_two_sorted_ll(list1, list2):
    if list1.head is None:
        return list2
    if list2.head is None:
        return list1
    merged_list = BasicOperations.LinkedList()
    l1 = list1.head
    l2 = list2.head
    if l1.data < l2.data:
        merged_list.head = list1.head
        l1 = l1.next
    else:
        merged_list.head = list2.head
        l2 = l2.next
    temp = merged_list.head
    while l1 is not None and l2 is not None:
        if l1.data > l2.data:
            temp.next = l2
            l2 = l2.next
            temp = temp.next
        else:
            temp.next = l1
            l1 = l1.next
            temp = temp.next
    if l1 is not None:
        temp.next = l1
    if l2 is not None:
        temp.next = l2
    return merged_list


if __name__ == '__main__':
    list1 = BasicOperations.LinkedList()
    list1.insert_values([-4,-3,-2,9])
    list2 = BasicOperations.LinkedList()
    list2.insert_values([-7,-6,-1,8,10,11])
    merged_list = merge_two_sorted_ll(list1,list2)
    merged_list.display()