import time
import os
import shellutils.stat

# def child():
#     print("\nA new child ", os.getpid())
#     while True:
#         print("Learn to attach to me: child.")
#         time.sleep(2)
#     # os._exit(0)

def execute(args):
    """Executes user-submitted commands with argument support."""
    if len(args) == 0:
        return False

    command = args[0]
    # parse input
    # ... 
    shellutils.stat.record_command(command)

    if command == "stat":
        for record in shellutils.stat.execute():
            print(record, end="")
    elif command == "exit":
        shellutils.stat.cleanup()
        return True
    elif command == "fork":
        # newpid = os.fork()
        # if newpid == 0:
        #     child()
        # else:
        #     while True:
        #         print("Learn to attach to me: parent")
        #         time.sleep(2)
        #     print("newpid ", newpid)
        #     pids = (os.getpid(), newpid)
        #     print("parent: %d, child: %d\n" % pids)
        print("to be implemented")   
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
            break

loop()
