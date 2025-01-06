class Stack():
    def __init__(self):
        # Initialize an empty stack
        self.stack = []
    
    def push(self, value):
        # Add the value to the top of the stack
        return self.stack.append(value)
    
    def pop(self):
        # Remove the value from the top of the stack
        return self.stack.pop()

    def peek(self):
        # Return the value at the top of the stack
        return self.stack[-1]

    def is_empty(self):
        # Check if the stack is empty, if so return None 
        if len(self.stack) == 0:
            return None 

# Examples
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek()) # 3
print(stack.pop()) # 3
print(stack.is_empty()) # None


