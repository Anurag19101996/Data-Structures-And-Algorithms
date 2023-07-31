#We need to add a method to the existing Linked List class (without tail pointer) to partition it such that for an integer x, we have a linked list with values lesser than x and another linked list greater than or equal to x. Then we need to concatenate these two linked lists in increasing order of values.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    
    def partition_list(self, m):
        if self.length == 0:
            return None
        #d1 is for smaller than m
        d1 = Node(0)
        #d2 is for greater than OR Equal m
        d2 = Node(0)
        p1 = d1
        p2 = d2
        temp = self.head
        after = temp.next
        while temp:
            if temp.value < m:
                temp.next = None
                p1.next = temp
                p1 = p1.next
                temp = after
                if after == None:
                    break
                after = after.next
            elif temp.value >=m:
                temp.next = None
                p2.next = temp
                p2=p2.next
                temp = after
                if after == None:
                    break
                after = after.next
           
        x1 = p1
        p1.next = d2
        p1 = p1.next.next
        x1.next = p1
        if self.head.value > m:
            self.head = d1
            self.head = self.head.next
        d1.next = None
        return self.print_list()

