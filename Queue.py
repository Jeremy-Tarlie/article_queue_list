from Node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None  
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:  
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):
        if self.head is None: 
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None: 
            self.tail = None
        return data
    
    def isEmpty(self):
        return self.head is None
    
    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count