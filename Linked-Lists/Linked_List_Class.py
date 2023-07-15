#We create a Linked Linked class with various methods to update it

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
     
    def append(self, value):
        new_node = Node(value)
        if self.head.value and self.tail.value == None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

  #THIS IS ORIGINAL POP BELOW:  
    def pop(self):
        if self.head == None and self.tail == None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            pre = self.head
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1
        
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True
            
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head == None
            self.tail == None
        temp = self.head
        self.head = self.head.next
        temp.next= None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index <0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        new_node = Node(value)
        if index <0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
       
        temp = self.get(index)
        pre = self.get(index-1)
        pre.next = new_node
        new_node.next = temp
        self.length +=1
        return True
    
    def remove(self, index):
        if self.length == 0:
            return None
        elif self.length == 1:
            if index != 0:
                return False
            else:
                self.head = None
                self.tail = None
        elif index <0 or index >= self.length:
            return False
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            pre = self.get(index-1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        if self.length >1 :
            after = temp.next
            before = None
            
            
            for i in range(0, self.length):
                if after == self.head:
                    after.next = temp
                    
                temp.next = before
                before = temp
                temp = after
                after = after.next
        return True


