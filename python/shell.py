import time

# Responsible for storing history of shell commands
history = []

def recordCommand(command):
    """Records each shell command along with the system time.

    Args:
        command -- The command entered by the user
    """
    fullstring = ""
    fullstring += time.strftime("%H:%M", time.localtime())
    fullstring += " " + command
    history.append(fullstring)

def stat():
    """Built-in command that displays a user's command history.

    Displays the history of commands received from the user along with the
    system time when it was input by the user.

    Returns:
        A list that stores a user's command history. Each element is string
        specifying the command entered and the system time at that time.
    """
    return history

def execute(args):
    """Executes user-submitted commands with argument support."""
    if len(args) == 0:
        return False

    command = args[0]
    # parse input
    # ...
    # always call stat
    recordCommand(command)

    if command == "stat":
        thishistory = stat()
        for com in thishistory:
            print(com)
    if command == "exit":
        return True

    return False

def loop():
    """Runs the main shell loop."""
    while True:
        print("> ", end="")
        # Tokenize input
        line = input()
        args = line.split()
        status = execute(args)
        # Check if user wants to exit shell
        if status:
            break;

loop()
