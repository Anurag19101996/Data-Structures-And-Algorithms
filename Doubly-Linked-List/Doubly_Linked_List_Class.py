#rememeber first shift the prev/next then Pointers.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self, value):
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            #below is wrong since head will be at the starting
            #new_node.prev = self.head
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            x1 = self.head
            self.head = None
            self.tail = None
            return x1
        x1 = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        x1.prev = None
        self.length -=1
        return x1
            
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = self.head.prev
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            x1 = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return x1
        else:
            x1 = self.head
            self.head = self.head.next
            x1.next = None
            self.head.prev = None
            self.length -= 1
            return x1
        
    def get(self, index):
        if self.length == 0:
            return None
        if index <0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
                if temp == None:
                    break
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp
    
    def set(self, index, value):
        temp = self.get(index)
        if temp == None:
            return False
        temp.value = value
        return True
    
    def insert(self, index, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.prepend(value)
            return True
        elif index == self.length:
            self.append(value)
            return True
        else:
            temp = self.head
            after = temp.next
            
            for i in range(index-1):
                temp = temp.next
                after = after.next
            
            temp.next = new_node
            after.prev = new_node
            new_node.prev = temp
            new_node.next = after
            self.length += 1
            return True

    def remove(self, index):
        if index <0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        pre = temp.prev
        after = temp.next
        
        temp.next = None
        temp.prev = None
        
        pre.next = after
        after.prev = pre
        
        self.length -= 1
        return temp
            
