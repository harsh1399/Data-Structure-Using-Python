class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def insert_beginning(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
        else:
            new_node = Node(value)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def insert_middle(self, value, position):
        if position <= 0 or position > self.get_length():
            raise Exception("Invalid Position")
        elif position == 1:
            self.insert_beginning(value)
        else:
            new_node = Node(value)
            temp = self.head
            prev = temp
            count = 0
            while count != position-1:
                prev = temp
                temp = temp.next
                count += 1
            new_node.next = temp
            new_node.prev = prev
            temp.prev = new_node
            prev.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data," ",end='',sep='')
            temp = temp.next
        else:
            print("Null")

    def search_value(self,value):
        temp = self.head
        while temp:
            if temp.data == value:
                print("Value Found")
                return
            temp = temp.next
        else:
            print("Value Not Found")

    def delete_beginning(self):
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        del temp

    def delete_end(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None
        del temp

    def delete_middle(self, position):
        if position <= 0 or position > self.get_length():
            raise Exception("Invalid Position")
        elif position == 1:
            self.delete_beginning()
        elif position == self.get_length():
            self.delete_end()
        else:
            temp = self.head
            prev = temp
            count = 0
            while count != position-1:
                prev = temp
                temp = temp.next
                count += 1
            prev.next = temp.next
            temp.next.prev = prev
            del temp


if __name__ == '__main__':
    link_list = DoublyLinkedList()
    link_list.insert_beginning(3)
    link_list.insert_beginning(4)
    link_list.insert_end(10)
    link_list.display()
    link_list.insert_middle(2,1)
    link_list.display()
    link_list.insert_middle(5, 3)
    link_list.display()
    link_list.insert_middle(6, 4)
    link_list.display()
    link_list.search_value(6)
    link_list.delete_end()
    link_list.display()
    link_list.delete_middle(3)
    link_list.display()
    link_list.delete_beginning()
    link_list.display()

