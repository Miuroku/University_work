import math

# Firstly we have to define Stack class.
class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, element):
        new_element_of_stack = None
        if len(self.stack) != 0:
            new_min_element = min(element, self.stack[-1][1])
            new_element_of_stack = (element, new_min_element)            
        else:
            new_element_of_stack = (element, element)

        self.stack.append(new_element_of_stack)
    
    def pop(self):
        upper_element = self.stack.pop()
        return upper_element[0]
    
    def get_min(self):
        if len(self.stack) != 0:
            return self.stack[-1][1]
        else:
            # Returns inf cuz if we'll compare min el from several 
            # stacks that'll be a correct value or inf.
            return math.inf