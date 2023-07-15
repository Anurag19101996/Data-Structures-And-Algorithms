#The task of this object is to remove duplicates from a given linked list without utilizing the tail pointer.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next  
            
    def print_all(self):
        if self.length == 0:
            print("Head: None")
        else:
            print("Head: ", self.head.value)
        print("Length: ", self.length)
        print("\nLinked List:")
        if self.length == 0:
            print("empty")
        else:
            self.print_list()

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        
    def remove_duplicates(self):
        if self.length == 0:
            return None
        val = []
        temp = self.head
        after = temp.next
        before = Node(0)
        before.next = temp
        x1 = before
        while temp:
            node_val = temp.value
            
            if node_val in val:
                temp.next = None
                before.next = after
                temp = after
                self.length -= 1
                if after == None:
                    break
                after = after.next
            else:
                before = temp
                temp = after
                if after == None:
                    break
                after = after.next
            val.append(node_val)
        x1.next = None

