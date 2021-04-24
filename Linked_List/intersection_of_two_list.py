"""Given the heads of two singly linked-lists headA and headB, return the node at which the two
lists intersect. If the two linked lists have no intersection at all, return null."""

from Linked_List import BasicOperations


def intersect(list1, list2):
    counta = 0
    countb = 0
    tempa = list1.head
    tempb = list2.head
    while tempa:
        counta += 1
        tempa = tempa.next

    while tempb:
        countb += 1
        tempb = tempb.next

    difference = abs(counta - countb)
    tempa = list1.head
    tempb = list2.head
    for _ in range(difference):
        if counta > countb:
            tempa = tempa.next
        else:
            tempb = tempb.next
    while tempa is not None and tempb is not None:
        if tempa == tempb:
            return tempa
        tempa = tempa.next
        tempb = tempb.next
    return None


if __name__ == '__main__':
    list1 = BasicOperations.LinkedList()
    list1.insert_end(3)
    list1.head.next = BasicOperations.Node(4)
    list1.head.next.next = BasicOperations.Node(5)
    list1.head.next.next.next = BasicOperations.Node(7)
    list2 = BasicOperations.LinkedList()
    list2.insert_end(1)
    list2.head.next = list1.head.next
    intersection_point = intersect(list1, list2)
    if intersection_point:
        print(f"Intersection point:{intersection_point.data}")
    else:
        print("No intersection point")