class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None 

class LinkedList():
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.next = next

    # Inserts a new node at the end of the linked list
    def insert_node(self, value):
        new_node = Node(value)

        # If the head of the list is none, meaning the list is empty, point the head and tail pointers to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            # Otherwise, point the next value of the tail to the new node
            self.tail.next = new_node
            self.tail = new_node
        
        # Return the list
        return new_node.value
    
    def print_list(self):
        curr = self.head
        # While current pointer is not none
        while curr:
            # Initialize a current pointer to self.head and traverse through the list, move the current pointer to the next value
            print(curr.value)
            curr = curr.next
    
    def return_tail(self):
        if not self.tail:
            return None 
        else:
            return self.tail
            

    def reverse_list(self):
        # We start at the head of our list (A -> B -> C)
        curr = self.head
        prev = None 
        while curr:
            # We save the next value of the current node (B)
            next = curr.next
            # We set the next value of the current node to the previous value (None)
            curr.next = prev
            # We set the previous value to the current value (A)
            prev = curr
            # We set the current value to the next value (B)
            curr = next

        return prev 

# Examples
my_list = LinkedList()
# print(my_list.insert_node(0))
# print(my_list.insert_node(1))
# print(my_list.insert_node(2))
# print(my_list.insert_node(3))

# print(my_list.print_list())

# print(my_list.return_tail().value)

print(my_list.reverse_list())
