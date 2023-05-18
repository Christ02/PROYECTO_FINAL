from utils.data_structures.linked_list import Node
import utils.status as status_utils
import utils.commit as commit_utils
import utils.init as init_utils
from pyfiglet import Figlet
import pickle
import click
import time
import sys
import os


@click.group()
def cli():
    pass


@cli.command()
def banner():

    figlet = Figlet(font='slant')
    print(figlet.renderText('geet'))


@cli.command()
def status():

    path = status_utils.get_current_path()
    new_files = status_utils.scan_for_new_files(path)
    deleted_files = status_utils.scan_for_deleted_files(path)
    modified_files = status_utils.scan_for_modified_files(path)

    status_message = '''
    On branch 'master'

    Uncommited changes:
        (use "geet commit -m <comment>..." to commit these changes)
    ''' 
    print(status_message)

    files_changed = False

    for file in deleted_files:
        files_changed = True
        print('             deleted:', file, end='\n')
    
    for file in modified_files:
        files_changed = True
        print('             modified:', file, end='\n')

    for file in new_files:
        files_changed = True
        print('             added:', file, end='\n')

    if not files_changed:
        print('        < There are no changes in the repository... >')


@cli.command()
def init():

    path = status_utils.get_current_path()
    initial_files = init_utils.get_init_files()
    repo_exists = init_utils.file_exists(path, '.geet')

    if repo_exists:
        print('Invalid operation: a geet repository already exists in this directory.')
        return None

    user_input = input('Creating geet repository in {} [press enter to continue]: '.format(path))
    
    if user_input != "":
        print('Canceling...')
        sys.exit(0)
 
    print('Initializing...')
    time.sleep(1)
    os.mkdir('.geet')
    os.mkdir('.geet/objects')

    for file in initial_files:
        init_utils.write_file(file, initial_files[file])

    # Creates master branch (linked list)
    branch_master = init_utils.create_branch(path) # NOTE: Activity no. 1 function invocation
    time_stack = init_utils.create_time_stack(path)
    # Creates initial commit
    commit_tree = commit_utils.create_tree_object(path, 'Initial commit') # NOTE: Activity no. 2 main function call
    commit_utils.save_tree_object(path, commit_tree)
    branch_master.insert_last(Node(commit_tree.name, commit_tree.message, 'Angel Tortola', 'tortola@ufm.edu'))
    
    
    x = time.asctime(time.localtime(time.time()))
    y = str(x)
    print(x)
    
    time_stack.push(y)

    # Saves branch as pickle
    file_name = path + '.geet/branch'
    file_stack = path + '.geet/stack'  

    '''
    TODO no. 3: Persist branch

    => Everytime we make a commit, we need to persist the latest version of the branch. In here, we'll persist for the first time our branch after making the initial commit.

        - Using the file_name provided above, persist the branch_master object in a pickle.

    ⬇ Your code starts here:
    '''
    with open(file_name, 'wb') as object_file:
        pickle.dump(branch_master, object_file, pickle.HIGHEST_PROTOCOL)

    with open(file_stack, 'wb') as object_file:
        pickle.dump(time_stack, object_file, pickle.HIGHEST_PROTOCOL)
    '''
    ⬆ Your code ends here.
    '''    
    print('Geet repository successfully created.')
    

@cli.command()
@click.option('-u', help='Author\'s name')
@click.option('-e', help='Author\'s email address')
def config(u, e):

    '''
    TODO no. 4: User config command

    => We'll use a simple python list in order to persist the author's name and email address.

        - We'll be able to update the authors data by using the following command: 
            geet config -u <username> -e <email>

        - Insert the parameters received into a list. The resulting list should look like this:
            [<username>, <email>]
    
        - Once you have the list, persist it into an object called 'user_config' in the hidden .geet folder.

        - Display in console the new user and email set.

    ⬇ Your code starts here:
    '''
    user_config = [u, e]
    current_path = os.getcwd()
    
    
    file_path = os.path.join(current_path + '/.geet', 'userconfig.pickle')

    with open(file_path, 'wb') as file:
        pickle.dump(user_config, file)
        
    print('User: {} Email: {}'.format(user_config[0], user_config[1]))
    

    '''
    ⬆ Your code ends here.
    '''


@cli.command()
@click.option('-m', help='Commit message')
def commit(m):

    path = status_utils.get_current_path()
    previous_hash_dict = status_utils.read_current_hash_dict(path)
    current_hash_dict = status_utils.get_hash_dict(path)

    if current_hash_dict == previous_hash_dict:
        print('\n     < No changes have been done, cannot commit. >')
        sys.exit(0)
    
    status_utils.save_hash_dict(path) # New current hash dict is saved
    commit_tree = commit_utils.create_tree_object(path, m) # Creates commit tree object. NOTE: activity no. 2 call
    commit_utils.save_tree_object(path, commit_tree) # Saves commit in disk
    print('Creating commit with hash {}.'.format(commit_tree.name))
    print('Commit message: {}'.format(commit_tree.message))

    # Reads pickle and retrieves branch as linked list object
    branch_path = path + '.geet/branch'
    stack_path = path + 'geetr/stack'

    with open(branch_path, 'rb') as file:
        branch = pickle.load(file)

    '''
    TODO no. 5: Insert commit node

        => In the previous lines we just read our master branch object (Linked List), assigned to the 'branch' variable.

            - In this branch instance, use the insert_last(<node>) method to add the commit Node into the branch.

            - You'll need to create a Node object (node from Tree class, not LL). The 'name' and 'message' are already in the 'commit_tree' object.

            - To pass the 'username' and 'email' params, you'll have to read the previously persisted list (activity no. 4).

            - Lastly, overwrite the persisted version of the branch with the new one, just like you did in activity number 3.

    ⬇ Your code starts here:
    '''
    node = Node(commit_tree.name, commit_tree.message)

    #read usersnames and emails
    with open('.geet/user_config.pickle', 'rb') as file:
        user_config = pickle.load(file)

   
    node.username = user_config[0]
    node.email = user_config[1]

    
    branch.insert_last(Node(commit_tree.name, commit_tree.message, node.username, node.email))

    with open(stack_path, 'rb') as f:
        stack = pickle.load(f)

    x = time.asctime( time.localtime(time.time()) )
    y = str(x)
    print(x)

    stack.push(y)

    with open(branch_path, 'wb') as file:
        pickle.dump(branch, file, pickle.HIGHEST_PROTOCOL)

    with open(stack_path, 'wb') as object_file:
        pickle.dump(stack, object_file, pickle.HIGHEST_PROTOCOL)
    pass
    '''
    ⬆ Your code ends here.
    '''


@cli.command()
def log():

    path = status_utils.get_current_path()
    # Reads pickle and retrieves branch as linked list object
    branch_path = path + '.geet/branch'

    '''
    TODO no. 6: Read branch

        => In order to print a commit log, we'll need to bring to memory the persisted branch (Linked List). Then we'll need to reverse it so commits are printed from latest to oldest. 
        
            - Read the pickle saved at 'branch_path'.

            - Reverse the linked list with its reverse() method. 

    ⬇ Your code starts here:
    '''
    with open(branch_path, 'rb') as f:
        branch = pickle.load(f)

    branch.reverse()
    '''
    ⬆ Your code ends here.
    '''

    print('[HEAD]\n')

    for commit in branch:
        print('Commit hash:', commit.hash)
        print('Commit message:', commit.message)
        print('Commit author:', commit.author)
        print('Commit contact:', commit.email, '\n')

    print('[Beginning of time]')

@cli.command()
def historial():
    path = status_utils.get_current_path()
    branch_path = path + 'geet/stack'
    
    with open(branch_path, 'rb') as f:
        stack = pickle.load(f)
        
    print('last modification', stack.peek())

if __name__ == '__main__':
    cli()
