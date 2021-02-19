import Stack as myStack

class Queue:
    def __init__(self):
        self.stack1 = myStack.Stack()
        self.stack2 = myStack.Stack()
    
    def push(self, element):
        self.stack1.push(element)
    
    def pop(self):
        upper_element = None
        if len(self.stack2) == 0:
            # Move all the elements from "stack1" to "stack2".
            while len(self.stack1) != 0:
                temp_element = self.stack1.pop()
                self.stack2.push(temp_element)
        upper_element = self.stack2.pop()
        return upper_element
    
    def get_min(self):
        return min(self.stack1.get_min(), self.stack2.get_min())