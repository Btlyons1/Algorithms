'''A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer,
together with next pointer and data which are there in singly linked list.'''

class Node:
    def _init_(self, next=None, prev=None, data=None):
        self.next = next
        slef.prev = prev
        self.data = data

