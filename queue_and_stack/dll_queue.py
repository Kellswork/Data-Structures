import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# first in first out

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements? because queue is easily implemented on a linked list
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # add the value to the tail of the DDL
        self.storage.add_to_tail(value)
        # increment the size
        self.size += 1

    def dequeue(self):
        # check if the size is greater than 0
        if self.size > 0:
            # decrement the size of the counter
            self.size -= 1
            # remove head of DLL and return it
            return self.storage.remove_from_head()

    def len(self):
        return self.size
