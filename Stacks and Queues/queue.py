class Queue:
    def __init__(self):
        # Initialize an empty queue
        self.queue = []

    def enqueue(self, value):
        # Add the value to the end of the queue
        self.queue.append(value)

    def dequeue(self):
        # Remove the value from the beginning of the queue
        return self.queue.pop(0)
    
    def peek(self):
        # Return the value at the beginning of the queue
        return self.queue[0]
    
    def is_empty(self):
        # Check if the queue is empty, if so return None 
        if len(self.queue) == 0:
            return None
        

# Examples
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)   
queue.enqueue(3)
print(queue.peek()) # 1
print(queue.dequeue()) # 1
print(queue.is_empty()) # None