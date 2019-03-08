"""Simple Shell feature for recording and fetching session command history.
"""
import os
import time
HISTORY_FILEPATH = ""

# https://0x46.net/thoughts/2019/02/01/dotfile-madness/
if "XDG_DATA_HOME" in os.environ:
    HISTORY_FILEPATH = os.path.abspath(os.getenv("XDG_DATA_HOME") + "/.ss-history")
else:
    HISTORY_FILEPATH = os.path.abspath(os.getenv("HOME") + "/.local/share/.ss-history")

def record_command(command):
    """Records each shell command along with the system time.

    Keyword arguments:
        command -- The command entered by the user
    """
    formatted_time = time.strftime("%H:%M", time.localtime())
    record_entry = "{} {}".format(formatted_time, command)
    history_file = open(HISTORY_FILEPATH, "a")
    history_file.write("{}\n".format(record_entry))
    history_file.close()

def get_history():
    """Load and returns a session's command history."""
    history_file = open(HISTORY_FILEPATH)
    history = history_file.readlines()
    history_file.close()
    return history

def cleanup():
    """Close named pipe upon shell's exit."""
    os.remove(HISTORY_FILEPATH)

def execute():
    """Built-in command that displays a user's command history.

    Displays the history of commands received from the user along with the
    system time when it was input by the user.

    Returns:
        A list that stores a user's command history. Each element is string
        specifying the command entered and the system time at that time.
    """
    result = get_history()
    cleanup()
    return result
