"""Implements the chdir system call
"""
import os
PREVDIR = os.path.abspath(os.path.curdir)

def rec_curdir():
    """Records the current directory before changing."""
    global PREVDIR
    PREVDIR = os.path.abspath(os.path.curdir)

def execute(args):
    """General changing directory Input: 'cd {dirname}'.

    Keyword arguments:
        args -- directory that user wants to navigate to.
    """
    if len(args) == 1:
        # Navigate to user's home directory.
        rec_curdir()
        os.chdir(os.environ["HOME"])
    elif args[1] == ".":
        # Stay in current directory
        rec_curdir()
        return
    elif args[1] == "..":
        # up
        rec_curdir()
        os.chdir(os.pardir)
    elif args[1] == "-":
        last_dir()
    else:
        os.chdir(args[1])

def last_dir():
    """Change to user's last visited directory Input: 'cd -'."""
    prev = PREVDIR
    rec_curdir()
    os.chdir(prev)
