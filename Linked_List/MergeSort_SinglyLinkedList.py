from Linked_List import BasicOperations


def find_middle(node):
    fast = node
    slow = node
    while fast and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(first, second):
    head = None
    if first.data <= second.data:
        head = first
        first = first.next
    else:
        head = second
        second = second.next
    temp = head
    while first and second:
        if first.data > second.data:
            temp.next = second
            temp = second
            second = second.next
        else:
            temp.next = first
            temp = first
            first = first.next
    if first:
        temp.next = first
    if second:
        temp.next = second
    return head


def merge_sort(node):
    if node is None or node.next is None:
        return node
    middle = find_middle(node)
    second_list = middle.next
    middle.next = None
    head_first = merge_sort(node)
    head_second = merge_sort(second_list)
    sorted_list = merge(head_first,head_second)
    return sorted_list


if __name__ == '__main__':
    list1 = BasicOperations.LinkedList()
    list1.insert_values([3,2,6,5,9,8,10,11])
    head_sorted = merge_sort(list1.head)
    while head_sorted:
        print(head_sorted.data,"->",sep='',end='')
        head_sorted = head_sorted.next
    print("Null")