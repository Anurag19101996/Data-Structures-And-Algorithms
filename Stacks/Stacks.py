#The class is created to initiate a Stack Data Structure. We can use the typical lists and add or remove from the last element for O(1) time complexity, but to make it more challenging we will recreate it in the same fashion as a linked list structure.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
            
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
            
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
