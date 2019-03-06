import time
history = []

def recordCommand(command):
    fullstring = ""
    fullstring += time.strftime("%H:%M", time.localtime())
    fullstring += " " + command
    history.append(fullstring)

def stat():
    return history

def execute(args):
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
    while True:
        print("> ", end="")
        line = input()
        args = line.split()
        status = execute(args)

        if status:
            break;

loop()
