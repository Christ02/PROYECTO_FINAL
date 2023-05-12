'''
[Data Structure] Linked List implementation.
'''


class Node:
    '''
    Node object.

    Attributes:
        hash (str): commit's hash
        message (str): commit's message
        author (str): user's name
        email (str): user's email
        next (Node): pointer to next node in list
    '''

    def __init__(self, hash: str, message: str, author: str, email: str, next_node=None):
        self.hash = hash
        self.message = message
        self.author = author
        self.email = email
        self.next = next_node

    def __str__(self):
        return f"{self.hash} - {self.message}"


class LinkedList:
    '''
    Linked List object.

    Attributes:
        start (Node): pointer to first node in list

    Methods:
        __init__(self)
        __iter__(self)
        traverse(self)
        insert_first(self, node)
        insert_last(self, node)
        remove(key)
        reverse(self)
    '''

    def __init__(self):
        self.start = None

    def __iter__(self):
        current_node = self.start
        while current_node:
            yield current_node
            current_node = current_node.next

    def traverse(self):
        current_node = self.start
        while current_node:
            print(current_node)
            current_node = current_node.next

    def insert_first(self, node):
        node.next = self.start
        self.start = node

    def insert_last(self, node):
        if not self.start:
            self.start = node
        else:
            current_node = self.start
            while current_node.next:
                current_node = current_node.next
            current_node.next = node

    def remove(self, key):
        current_node = self.start
        previous_node = None
        found = False
        while current_node and not found:
            if current_node.hash == key:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.next
        if current_node is None:
            raise ValueError("Key not found in list")
        if previous_node is None:
            self.start = current_node.next
        else:
            previous_node.next = current_node.next

    def reverse(self):
        previous_node = None
        current_node = self.start
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.start = previous_node
