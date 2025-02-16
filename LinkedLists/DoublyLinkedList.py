class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

        return self
    
    def reverse_print_list(self):
        curr = self.tail
        while curr:
            print(curr.value)
            curr = curr.prev
    
    def pop(self):
        if self.length == 0:
            return None 
        
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None 
        self.length -= 1 
        
        if self.length == 0:
            self.head = None 
            self.tail = None 

        return temp
    
    
    



# Examples
my_list = DoublyLinkedList(7)
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list.pop().value)