# Course: CS261 - Data Structures
# Assignment: 5
# Student: Leonel Garay
# Description: Implement the MinHeap class by completing provided skeleton code.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap maintaining heap property.
        """
        self.heap.append(node)  # Appends node to heap.
        self.add_helper(self.heap.length() - 1)  # Starts add_helper.

    def add_helper(self, index):
        """
        Helper for add function. Identifies where to place the new node and trades places with parent if greater.
        """
        parent = ((index - 1) // 2)  # Identifies parent.
        while self.heap.get_at_index(index) < self.heap.get_at_index(parent) and index != 0:  # If index is less than
            # parent and not equal to 0.
            self.heap.swap(parent, index)  # Swap values.
            index = parent  # Updates value index to parent.
            parent = ((index - 1) // 2)  # Identifies the new parent.
        return

    def get_min(self) -> object:
        """
        Returns an object with a minimum key without removing it from the heap.
        """
        if self.is_empty() is True:  # Raises exception if heap is empty.
            raise MinHeapException()
        return self.heap.get_at_index(0)  # Returns index 0.

    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise MinHeapException()
        return None

    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())
    #
    # print("\nPDF - build_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)
