"""Main Simple Shell loop.
"""
import os
import shellutils.stat

def ss_launch(args):
    """Launches external, non-builtin process"""
    # TODO TEST FOR NO ARGS
    # TODO Replace manual fork calls with subprocess module
    child_pid = os.fork()  # https://www.python-course.eu/forking.php
    if child_pid == 0:
        # Child process.
        if args[0] == "":
            return  # Blank line entered, do nothing
        else:
            # TODO Docuemt difference: subprocess.call(command + arg_list)
            os.execvp(args[0], args)
        os._exit(0)  # TODO Figure out better exit code.
    elif child_pid < 0:
        print("There was an error forking process.")
    else:
        # Parent process.
        os.waitpid(child_pid, 0) # Destructure into pid, status
        # print ("wait returned, pid = {}, status = {}".format(pid, status))

def ss_execute(args):
    """Executes user-submitted commands with argument support."""
    if len(args) == 0:
        return False

    command = args[0]
    # parse input
    # ...
    shellutils.stat.record_command(command)

    if command == "exit":
        shellutils.stat.cleanup()
        return True
    elif command == "stat":
        for record in shellutils.stat.execute():
            print(record, end="")
    else:
        ss_launch(args)
    return False

def ss_loop():
    """Runs the main shell loop."""
    while True:
        print("> ", end="")
        # Tokenize input
        line = input()
        args = line.split()
        status = ss_execute(args)
        # Check if user wants to exit shell
        if status:
            break

ss_loop()
