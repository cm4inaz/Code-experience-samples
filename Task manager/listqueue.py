"""
listqueue.py
11/30/2024
A list-based implementation of stacks.
"""

class ListQueue(object):

    # Constructor
    def __init__(self, source_collection=None):
        if source_collection is None:
            self.items = []
        else:
            self.items = list(source_collection)

    # Accessor methods
    def is_empty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self.items)

    def __str__(self):
        size = len(self)
        result = "{"
        if size > 0:
            for i in range(0, size - 1):
                result += str(self.items[i]) + ", "
            result += str(self.items[-1])

        result += "}"
        return result

    def __iter__(self):
        for item in self.items:
            yield item

    def __add__(self, other):
        if isinstance(other, ListQueue):
            return ListQueue(self.items + other.items)
        else:
            raise TypeError("Cannot add non ListStack")

    def __eq__(self, other):
        if isinstance(other, ListQueue):
            return self.items == other.items
        else:
            return False

    def peek(self):
        """Returns the item at the front of the queue.
        Raises IndexError if queue is not empty."""
        if len(self) > 0:
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items.clear()

    def add(self, item):
        """Inserts item at the rear of the queue."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item at the front of the
        queue. Raises IndexError if queue is not empty."""
        return self.items.pop(0)

    def remove(self, item):
        """Removes the specified item from the items list"""
        self.items.remove(item)
