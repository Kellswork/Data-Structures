import sys

sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# last in first out, push and pop. a real stack only lets these two functions happen in them


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? because stack is easily implemented on a linked list
        self.storage = DoublyLinkedList()

    def push(self, value):
        # add the value to the head of the DDL
        self.storage.add_to_head(value)
        # increment the size
        self.size += 1

    def pop(self):
        # check if the size is greater than 0
        if self.size > 0:
            # decrement the size of the counter
            self.size -= 1
            # remove head of DLL and return it
            return self.storage.remove_from_head()

    def len(self):
        return self.size
