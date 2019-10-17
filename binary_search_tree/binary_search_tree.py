import sys

sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # return value if self.value == value
        # if value == self.value:
        #     return
        if value < self.value:
            # checks if the left has a child
            if self.left is None:
                # if it have a value doesn't we assign it value and return
                self.left = BinarySearchTree(value)

            else:
                # if it does, we change the root to the current value
                self.left.insert(value)

        elif value >= self.value:
            # checks if the left has a child
            if self.right is None:
                # if it doesn't we assign it value and return
                self.right = BinarySearchTree(value)

            else:
                # if it does, we change the root to the current value
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if value is == to self.value, return value
        if self.value == target:
            return True

        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        if target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # BASE CASE
        # if empty tree
        if not self:
            # return none
            return None

        max_value = self.value
        # get a ref to current node
        current_node = self
        # check if we are at a valid tree node
        while current_node:
            # if our current value is greater than the max value
            if current_node.value > max_value:
                # update the max value
                max_value = current_node.value
            # move on to the next right node in the tree
            # setting the current node to the current nodes right
            current_node = current_node.right
        # return our max value
        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # base case
        cb(self.value)
        # left case
        if self.left:
            self.left.for_each(cb)
        # right case
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
