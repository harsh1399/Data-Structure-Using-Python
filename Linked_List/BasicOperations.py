class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

    def __eq__(self, other):
        if self.data == other.data and self.next == other.next:
            return True

class LinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        count = 0
        temp = self.head
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
            self.head = new_node

    def insert_end(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            new_node = Node(value)
            temp.next = new_node

    def insert_middle(self, value, position):
        if position <= 0 or position > self.get_length():
            raise Exception("Invalid Position")
        elif position == 1:
            self.insert_beginning(value)
        else:
            count = 0
            temp = self.head
            prev = temp
            while count != position-1:
                prev = temp
                temp = temp.next
                count += 1
            new_node = Node(value)
            new_node.next = prev.next
            prev.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data,"-->",end='',sep='')
            temp = temp.next
        else:
            print("Null")

    def search(self,value):
        temp = self.head
        while temp:
            if temp.data == value:
                print("Value Found")
                break
            temp = temp.next
        else:
            print("Value Not Found")

    def remove_beginning(self):
        temp = self.head
        self.head = temp.next
        del temp

    def remove_end(self):
        temp = self.head
        prev = temp
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None
        del temp

    def remove_middle(self,position):
        if position <= 0 or position > self.get_length():
            raise Exception("Invalid Position")
        elif position == 1:
            self.remove_beginning()
        elif position == self.get_length():
            self.remove_end()
        else:
            temp = self.head
            prev = temp
            count = 0
            while count != position-1:
                prev = temp
                temp = temp.next
                count += 1
            prev.next = temp.next
            del temp

    def delete(self):
        self.head = None

    def insert_values(self,data_list):
        for value in data_list:
            if self.head is None:
                new_node = Node(value)
                self.head = new_node
            else:
                self.insert_end(value)


if __name__ == '__main__':
    link_list = LinkedList()
    link_list.insert_beginning(10)
    link_list.insert_end(20)
    link_list.insert_end(30)
    link_list.insert_end(40)
    link_list.display()
    link_list.insert_middle(50,2)
    link_list.display()
    link_list.insert_middle(60,1)
    link_list.display()
    link_list.insert_middle(70, 6)
    link_list.display()
    link_list.search(80)
    link_list.remove_middle(3)
    link_list.display()
    link_list.remove_beginning()
    link_list.display()
    link_list.remove_end()
    link_list.display()
    link_list.remove_middle(link_list.get_length())
    link_list.display()
    link2 = LinkedList()
    link2.insert_values([1,7,8,9,10])
    link2.display()