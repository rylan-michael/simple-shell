def execute(args):
    """Executes user-submitted commands with argument support."""
    if len(args) == 0:
        return False

    command = args[0]
    # parse input
    # ... 
    recordCommand(command)

    if command == "stat":
        history = stat()
        for com in history:
            print(com)
    elif command == "exit":
        return True
    elif command == "fork":
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            while True:
                print("Learn to attach to me: parent")
                time.sleep(2)
            print("newpid ", newpid)
            pids = (os.getpid(), newpid)
            print("parent: %d, child: %d\n" % pids)
            
    return False