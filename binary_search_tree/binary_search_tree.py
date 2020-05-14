"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        searching = True
        current = self
        # searching for valid spot
        while searching:
            # test if value is smaller
            if value < current.value:
                # if smaller and No value insert node
                if current.left == None:
                    current.left = BinarySearchTree(value)
                    searching = False
                # if smaller and left node has value go left
                else:
                    current = current.left
            # value is >= move right
            else:
                # if no value right insert node
                if current.right == None:
                    current.right = BinarySearchTree(value)
                    searching = False
                # if larger and right node has value go right
                else:
                    current = current.right

        # Return True if the tree contains the value
        # False if it does not
    def contains(self, target):
        # when we start, self will be the root
        # compare the target against self
        if target == self.value:
            return True
        # if target > self.value go right else go left
        if target > self.value:
            if not self.right:
                return False
            # go right
            return self.right.contains(target)
        else:
            if not self.left:
                return False
            # go left
            return self.left.contains(target)

        # Return the maximum value found in the tree
    def get_max(self):
        pass
        # current = self
        # while current.right != None:
        #     current = current.right
        # return current.value

        # Call the function `fn` on the value of each node

    def for_each(self, fn):
        pass
        # array to hold all nodes on the right to come back to
        # rights = []
        # current = self
        # searching = True
        # # while loop runs until at a leaf and nothing in rights list
        # while searching:
        #     if current.right is not None:
        #         rights.append(current.right)
        #     if current.left is not None:
        #         current = current.left
        #         fn(current)
        #     else:
        #         current = rights.pop(0)

        # current = self
        # fn(current.value)
        # current = self
        # print(current.value)
        # if current.left is not None or current.right is not None:
        #     fn(current.value)
        #     self.for_each(current.left)
        #     self.for_each(current.right)
        # Part 2 -----------------------

        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


def printing(node):
    print('node', node.value)


bst = BinarySearchTree(5)
bst.insert(2)
bst.for_each(printing)
print('bst', bst.left.value)
