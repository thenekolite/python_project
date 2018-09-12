class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def getSize(self):
        return self.size

    def addFirst(self, data):
        temp = Node(data)
        self.size += 1

        if self.isEmpty():
            self.head = temp
            self.tail = temp
        else:
            temp.next_node = self.head
            self.head = temp

    def addLast(self, data):
        temp = Node(data)
        self.size += 1

        if self.isEmpty():
            self.head = temp
            self.tail = temp
        else:
            self.tail.next_node = temp
            self.tail = self.tail.next_node

    def delete_data(self, data):
        temp = self.head

        if self.getSize() == 0:
            self.head = None
        else:
            if temp.data == data:
                self.head = temp.next_node
                self.size -= 1
            else:
                while temp.next_node != None:
                    if temp.next_node.data == data:
                        delete_node = temp.next_node
                        temp.next_node = temp.next_node.next_node
                        del(delete_node)
                        self.size -= 1
                    else:
                        temp = temp.next_node

    def display(self):
        temp = self.head

        while temp != None:
            print(f"{temp.data} ->", end=" ")
            temp = temp.next_node
        print("null")


linked_list = LinkedList()

linked_list.addFirst(5)
linked_list.addLast(10)
linked_list.addLast(20)
linked_list.addLast(25)
linked_list.addLast(30)
linked_list.display()
print(linked_list.getSize())

linked_list.delete_data(5)
linked_list.delete_data(20)
linked_list.delete_data(30)
linked_list.display()
print(linked_list.getSize())

linked_list.delete_data(10)
linked_list.delete_data(25)
linked_list.display()
print(linked_list.getSize())
linked_list.delete_data(10)
linked_list.display()
