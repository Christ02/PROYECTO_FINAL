'''
[Data Structure] Tree for storing a directory snapshot.
'''


class Node():
    '''
    Node object. Used to represent each file of the folder's filesystem. 

    Attributes:
        name (str): name of the file
        content (list): content of the file, represented as a list containing each line of the file as an element.
    '''
    def __init__(self, name: str, content: list):
        self.name = name
        self.content = content


class Tree(): 
    '''
    Tree object.

    Attributes:
        name (str): tree's name
        message (str): commit's message. Set to None in constructor.
        children (list): list of children (Nodes)

    Methods:
        __init__(self): receives 'name' as a param to instantiate the object
        insert_child(self, object): appends a Node to the tree's children list
        get_children(self): returns the tree's children list 
    '''
    
    '''
    TODO no. 2: Commit Tree

    => We'll use a Tree to save a snapshot of the current directory.

        - Based on those docstrings found in this Tree class, implement the needed methods.
    
    ⬇ Your code starts here:
    '''
    def __init__(self, name: str):
        self.name = name
        self.message = None
        self.children = []

    def insert_child(self, object):
        self.children.append(object)

    def get_children(self):
        return self.children
    '''
    ⬆ Your code ends here.
    '''
