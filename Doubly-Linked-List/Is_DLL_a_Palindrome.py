class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def is_palindrome(self):
        original_val = []
        temp = self.head
        while temp:
            original_val.append(temp.value)
            temp = temp.next
            
        if original_val == original_val[::-1]:
            return True
        else:
            return False


#alternative method to check for palindromes, this is better in terms of time complexity since we are not adding elements to a list and reversing consequently
# =============================================================================
#     def is_palindrome(self):
#         if self.length == 0:
#            return True
#         temp_h = self.head
#         temp_t = self.tail
#         if self.length %2 == 0:
#             half_length = self.length/2
#         elif self.length %2 != 0:
#             half_length = int(round(self.length/2,0)) + 1
#         
#         for _ in range(half_length):
#             if temp_t.value != temp_h.value:
#                 return False
#             else:
#                 return True
#             temp_h = temp_h.next
#             temp_t = temp_t.prev
# =============================================================================

#Test cases
my_dll_1 = DoublyLinkedList(1)
my_dll_1.append(2)
my_dll_1.append(3)
my_dll_1.append(2)
my_dll_1.append(1)

print('DLL1 is a palindrome')
print( my_dll_1.is_palindrome() )


my_dll_2 = DoublyLinkedList(1)
my_dll_2.append(2)
my_dll_2.append(3)

print('\nDLL2 is a palindrome')
print( my_dll_2.is_palindrome() )

my_dll_3 = DoublyLinkedList(1)
print('\nDLL3 is a palindrome')
print( my_dll_3.is_palindrome())

