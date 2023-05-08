# Geet

Geet is an educational git alternative, developed to understand git's internals.


## Installation

First, go the project's folder: 
> `$ cd geet`

Then you might want to create a new virtual environment for the proyect:
> `$ mkdir venv`  
> `$ python3 -m venv venv`  
> `$ source venv/bin/activate`  

Once your new environment is activate, install the required dependencies by executing:
>`$ pip install -r requirements.txt`


To be able to run the *geet* command in your terminal, you need to create an alias in your `.bashrc` or `.zshrc` file.


### Zsh

Go to your filesystem's root:
> `$ cd ~`  

In your `.bashrc`  or`.zshrc` file, add the following line and save the changes:  
> `alias geet='python {path-to-your-repo}/geet/main.py'`

After restarting your terminal, you should be able to execute:  

> `$ geet`  

And receive an output like this:   
<pre>
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  banner
  commit
  config
  init
  log
  status              
</pre>

Now you are ready to start working on your activities :).
