class Node:
    '''
    Node object for stack.

    Attributes:
        data: data stored in the node
        next_node: reference to the next node
    '''

    def _init_(self, data):
        self.data = data
        self.next_node = None


class Stack:
    '''
    Stack object, list-based implementation.

    Attributes:
        top (Node): pointer to the topmost node
    '''

    def _init_(self):
        self.top = None

    def _repr_(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next_node
        return 'Last time: {} '.format(elements)

    def push(self, value):
        '''
        Pushes element into the stack.

        Args:
            value: value to be inserted

        Returns:
            None
        '''
        new_node = Node(value)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        '''
        Pops element out of stack.

        Returns:
            value: value of element popped
        '''
        if self.is_empty():
            print('Stack underflow :(')
            return None

        value = self.top.data
        self.top = self.top.next_node
        return value

    def peek(self):
        '''
        Peeks topmost element.

        Returns:
            value: value of element peeked
        '''
        if self.is_empty():
            print('Stack underflow :(')
            return None

        return self.top.data

    def is_empty(self):
        '''
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise
        '''
        return self.top is None

    def search(self, key):
        '''
        Searches for the key in the stack.

        Args:
            key: value to search for

        Returns:
            index: index of the key in the stack, -1 if not found
        '''
        index = 0
        current = self.top
        while current:
            if current.data == key:
                return index
            current = current.next_node
            index += 1
        return -1