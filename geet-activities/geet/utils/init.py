'''
[Module] Init command utils.
'''
import os
import utils.data_structures.linked_list as linked_list
import utils.data_structures.stack as Stack


def write_file(name: str, lines: list) -> None:

    with open(name, 'w') as writer:
        writer.write('\n'.join(lines))


def get_init_files() -> dict:

    initial_files = {
        '.geet/.geetignore': [".DS_Store\n"],
        '.geet/.hashdict.json': ["{\"README.md\": \"1ea4b01b49eae1fd044238ae5423222eac5495ce\"}\n"],
        'README.md': ["### Geet", "Fresh geet repository.\n"]
    }

    return initial_files


def file_exists(path: str, name: str) -> bool:

    return os.path.exists(path + name)


def create_branch(path: str) -> object:

    '''
    TODO no. 1: Linked List branch

    => We'll use a Linked List to represent the master branch. Each commit will be a node in the LL.

        - In geet/utils/data_structures/linked_list.py you'll find the boilerplate for a linked list class. Based on those docstrings, implement a linked list.

        - Once your data structure is ready, create an empty instance and make it the return of this method.

    ⬇ Your code starts here:
    '''
    linkedlist = linked_list.LinkedList()
    return linkedlist
    '''
    ⬆ Your code ends here.
    '''

def create_time_stack(path: str) -> object:
    time_stack = Stack.Stack()
    return time_stack