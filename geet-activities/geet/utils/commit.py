'''
[Module] Commit command utils.
'''
import time
import pickle
import hashlib
from utils.data_structures.tree import Node, Tree
from utils.status import list_files, read_file_by_lines


def create_tree_object(path: str, commit_msg: str) -> object: 

    commit_tree = Tree("Commit Tree") # NOTE: Activity no. 2 structure instance
    files = list_files(path)
 
    # Adds every file in path as a child of type Node
    for file in files:

        file_content = read_file_by_lines(path + file)
        node = Node(file, file_content)   
        commit_tree.insert_child(node)

    children_str = str(commit_tree.get_children()) + str(time.time()) 
    commit_hash = hashlib.sha1(children_str.encode('utf-8')).hexdigest()
    commit_tree.name = commit_hash
    commit_tree.message = commit_msg

    return commit_tree


def save_tree_object(path: str, tree: object) -> None:

    file_name = path + '.geet/objects/' + tree.name

    with open(file_name, 'wb') as outp:
        pickle.dump(tree, outp, pickle.HIGHEST_PROTOCOL)

    return None
