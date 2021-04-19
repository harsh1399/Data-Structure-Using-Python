class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_beginning(self,value):
        if self.head == None:
            new_node = Node(value)
            self.head = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def insert_end(self,value):
        temp = self.head
        while(temp.next != None):
            temp =temp.next
        new_node = Node(value)
        temp.next = new_node

    def insert_middle(self,value,position):
        count = 0
        temp = self.head
        prev = temp
        if position == 0:
            self.insert_beginning(value)
        while(count != position):
            prev = temp
            temp =temp.next
            count += 1
        new_node = Node(value)
        new_node.next = prev.next
        prev.next = new_node

    def display(self):
        temp = self.head
        while(temp != None):
            print(temp.data,"-->",end='',sep='')
            temp = temp.next
        else:
            print("None")

    def search(self,value):
        temp = self.head
        while(temp.next != None):
            if temp.data == value:
                print("Value Found")
                break
            temp = temp.next
        else:
            print("Value Not Found")

if __name__ == '__main__':
    link_list = Linked_List()
    link_list.insert_beginning(10)
    link_list.insert_end(20)
    link_list.insert_end(30)
    link_list.insert_end(40)
    link_list.display()
    link_list.insert_middle(50,2)
    link_list.display()
    link_list.insert_middle(60,0)
    link_list.display()
    link_list.insert_middle(70, 7)
    link_list.display()
    link_list.search(80)